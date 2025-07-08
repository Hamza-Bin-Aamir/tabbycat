def is_staff(context):
    if context is None or 'view' not in context:
        return False
    user = getattr(context.get('request'), 'user', None)
    return user and hasattr(user, 'is_staff') and user.is_staff