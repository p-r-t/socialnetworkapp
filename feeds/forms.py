from flask_wtf import Form
from wtforms import validators, StringField
from wtforms.widgets import TextArea
from flask_wtf.file import FileAllowed, FileField

from feeds import errors


class FeedPostForm(Form):
    """The feed post form allows the user to post images and post to the feed home page"""

    images = FileField("Select images",
                       render_kw={"multiple": True},
                       validators=[
                           FileAllowed(['jpg', "jpeg", "png", "gif"], errors.FILE_TYPES)

                       ]
                       )

    post = StringField("Post", widget=TextArea(), validators=[validators.DataRequired(), validators.Length(max=1024)])
