from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TelegramForm(FlaskForm):

    title = StringField('Title',
                        validators=[
                                    DataRequired(),
                                    Length(min=5, max=25)
                                    ])
    signature = StringField('Signature',
                            validators=[
                                        DataRequired(),
                                        Length(min=5, max=25)
                                        ])
    telegram = TextAreaField("Telegram",
                             validators=[
                                        DataRequired(),
                                        Length(min=5, max=2500)
                                        ])
    submit = SubmitField('Telegraph')
