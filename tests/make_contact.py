from fogstreamtest.apps.contact.models import ContactMessage


def make_contact(author, attributes):
    return ContactMessage.objects.create(title=attributes['title'], body=attributes['body'], author_id=author.id)
