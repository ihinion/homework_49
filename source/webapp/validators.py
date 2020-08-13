from django.core.exceptions import ValidationError


def at_least_200(string):
    if len(string) <= 200:
        raise ValidationError('This text has 200 or less characters, '
                              'consider putting it into "description" field instead')


def min_30(string):
    if len(string) < 30:
        raise ValidationError('This description is less than 30 characters and therefore too short, '
                              'your project manager will not be happy, try to be more specific')


def no_caps(string):
    if string.isupper():
        raise ValidationError('Did you forget to turn off CapsLock?')


def restricted_text_art(string):
    art = ['( ノ-_-)ノ~┻━┻', '(╯ಠ ‿ಠ)╯︵┻━┻', '(ﾉ>｡<)ﾉﾐ┻┻', '(ﾉ｀□´ )ﾉ⌒┻━┻']
    for i in art:
        if i in string:
            raise ValidationError("Don't throw furniture around here!")

