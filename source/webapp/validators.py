from django.core.exceptions import ValidationError


def at_least_200(string):
    if len(string) <= 200:
        raise ValidationError('This text has 200 or less characters, '
                              'consider putting it into "description" field instead')


def restricted_text_art(string):
    art = ['( ノ-_-)ノ~┻━┻', '(╯ಠ ‿ಠ)╯︵┻━┻', '(ﾉ>｡<)ﾉﾐ┻┻', '(ﾉ｀□´ )ﾉ⌒┻━┻']
    for i in art:
        if i in string:
            raise ValidationError("Don't throw furniture around here!")

