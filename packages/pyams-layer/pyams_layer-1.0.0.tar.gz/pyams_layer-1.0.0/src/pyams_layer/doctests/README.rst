===================
PyAMS_layer package
===================

Introduction
------------

This package is composed of a set of utility functions, usable into any Pyramid application.

    >>> from pyramid.testing import setUp, tearDown, DummyRequest
    >>> config = setUp()

    >>> from pyams_utils.request import get_annotations
    >>> config.add_request_method(get_annotations, 'annotations', reify=True)

    >>> from pyams_utils import includeme as include_utils
    >>> include_utils(config)
    >>> from pyams_layer import includeme as include_layer
    >>> include_layer(config)


Skinning a request
------------------

    >>> from pyams_layer.interfaces import ISkin, PYAMS_BASE_SKIN_NAME
    >>> from pyams_layer.skin import PyAMSSkin
    >>> config.registry.registerUtility(PyAMSSkin, provided=ISkin, name=PYAMS_BASE_SKIN_NAME)

    >>> from pyams_layer.skin import apply_skin
    >>> request = DummyRequest()
    >>> apply_skin(request, PYAMS_BASE_SKIN_NAME)

    >>> from pyams_layer.skin import get_skin
    >>> skin = get_skin(request)
    >>> skin
    <class 'pyams_layer.skin.PyAMSSkin'>
    >>> skin.layer
    <InterfaceClass pyams_layer.interfaces.IPyAMSLayer>
    >>> skin.layer.providedBy(request)
    True


Skinning contents
-----------------

When a skin is applied on "skinnable" content, this skin is automatically applied to request
during traversal:

    >>> from zope.container.folder import Folder
    >>> from pyams_layer.skin import UserSkinnableContentMixin
    >>> class Content(UserSkinnableContentMixin, Folder):
    ...     """Skinnable content"""

    >>> root = Folder()
    >>> content = Content()
    >>> root['content'] = content
    >>> content.skin = PYAMS_BASE_SKIN_NAME
    Traceback (most recent call last):
    ...
    zope.schema._bootstrapinterfaces.ConstraintNotSatisfied: ('PyAMS base skin', 'skin')

In fact, "PyAMS base skin" is the default skin, we can only set custom skins inheriting from it:

    >>> from zope.interface import implementer
    >>> from pyams_layer.interfaces import IPyAMSUserLayer

    >>> class IMyCustomLayer(IPyAMSUserLayer):
    ...     """Custom skin layer"""

    >>> class MyCustomSkin:
    ...     label = "My custom skin"
    ...     layer = IMyCustomLayer

    >>> config.registry.registerUtility(MyCustomSkin, provided=ISkin, name=MyCustomSkin.label)

    >>> content.skin = MyCustomSkin.label
    >>> content.skin
    'My custom skin'
    >>> content.can_inherit_skin
    False
    >>> content.inherit_skin
    False
    >>> content.inherit_skin = True
    >>> content.inherit_skin
    False
    >>> content.skin_parent is content
    True
    >>> content.get_skin(request)
    <class 'pyams_layer.tests.test_utilsdocs.MyCustomSkin'>

    >>> from zope.traversing.interfaces import BeforeTraverseEvent
    >>> from pyams_layer.skin import handle_content_skin
    >>> request = DummyRequest()
    >>> handle_content_skin(BeforeTraverseEvent(content, request))
    >>> get_skin(request) is MyCustomSkin
    True

Let's try to create an inner content:

    >>> subcontent = Content()
    >>> content['subcontent'] = subcontent
    >>> subcontent.can_inherit_skin
    True
    >>> subcontent.inherit_skin
    False
    >>> subcontent.inherit_skin = True
    >>> subcontent.inherit_skin
    True
    >>> subcontent.skin_parent is content
    True
    >>> subcontent.get_skin(request)
    <class 'pyams_layer.tests.test_utilsdocs.MyCustomSkin'>

    >>> request = DummyRequest()
    >>> handle_content_skin(BeforeTraverseEvent(subcontent, request))
    >>> get_skin(request) is None
    True

Here, skin is None because as subcontent is inheriting skin from it's parent, skin should have
been applied during traversal of parent object:

    >>> request = DummyRequest()
    >>> handle_content_skin(BeforeTraverseEvent(content, request))
    >>> handle_content_skin(BeforeTraverseEvent(subcontent, request))
    >>> get_skin(request) is MyCustomSkin
    True


Tests cleanup:

    >>> tearDown()
