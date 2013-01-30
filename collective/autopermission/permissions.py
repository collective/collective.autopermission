import Products
from AccessControl.Permission import _registeredPermissions
from AccessControl.Permission import pname
from AccessControl.Permission import ApplicationDefaultPermissions

# This is borrowed from Products.CMFCore.permissions to avoid a dependency.

addPermission = None
try:
    from AccessControl.Permission import addPermission
except ImportError:
    pass

def setDefaultRoles(permission, roles):
    '''
    Sets the defaults roles for a permission.
    '''
    if addPermission is not None:
        addPermission(permission, roles)
    else:
        # BBB This is in AccessControl starting in Zope 2.13
        import Products
        registered = _registeredPermissions
        if not registered.has_key(permission):
            registered[permission] = 1
            Products.__ac_permissions__=(
                Products.__ac_permissions__+((permission,(),roles),))
            mangled = pname(permission)
            setattr(ApplicationDefaultPermissions, mangled, roles)


def create_permission(permission, event):
    """When a new IPermission utility is registered (via the <permission />
    directive), create the equivalent Zope2 style permission.
    """
    setDefaultRoles(permission.title, ('Manager',))
