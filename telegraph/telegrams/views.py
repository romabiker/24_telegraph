from datetime import date
import os


from flask import (
    abort,
    Blueprint,
    current_app as app,
    json,
    redirect,
    render_template,
    url_for,
    safe_join,
    session,
)
from werkzeug import secure_filename


from slugify import slugify  # it can convert russian title into inglish slug


from .forms import TelegramForm
from telegraph.utils import get_secret_key, get_random_string


telegrams_blueprint = Blueprint(
    'telegram', __name__,
    template_folder='../templates/telegrams',
)


def make_slug_from(date, title, slug=None):
    if not slug:
        slug = secure_filename('-'.join([str(date.month),
                                         str(date.day),
                                         slugify(title,
                                                 max_length=30,
                                                 word_boundary=True,
                                                 save_order=True)]))
    if not os.path.exists(safe_join(app.config['TELEGRAMS_PATH'], slug)):
        return slug
    slug = '{}-{}'.format(slug, get_random_string(length=5))
    return make_slug_from(date, title, slug)


def check_in(telegram_dict):
    return telegram_dict['owner_key'] == session.get('owner_key')


def load_from_file_storage(slug):
    filename = safe_join(app.config['TELEGRAMS_PATH'], slug)
    with open(filename, 'r') as file_handler:
        return json.load(file_handler)


def load_from_file_storage_or_404(slug):
    try:
        return load_from_file_storage(slug)
    except FileNotFoundError as e:
        abort(404)


def dump_to_file_storage(telegram_dict):
    filename = safe_join(app.config['TELEGRAMS_PATH'], telegram_dict['slug'])
    with open(filename, 'w') as file_handler:
        json.dump(telegram_dict, file_handler)
    return None


def populate_from(form, owner_key, slug=None):
    if not slug:
        slug = make_slug_from(date.today(), form.title.data)
    return {
        'title': form.title.data,
        'telegram': form.telegram.data,
        'signature': form.signature.data,
        'slug': slug,
        'owner_key': owner_key,
    }


def telegraph_telegram(form, slug=None):
    if not session.get('owner_key'):
        session['owner_key'] = get_secret_key()
    telegram_dict = populate_from(form, session['owner_key'], slug)
    dump_to_file_storage(telegram_dict)
    return redirect(url_for('telegram.deliver',
                            slug=telegram_dict['slug']))


@telegrams_blueprint.route('/', methods=['GET', 'POST'])
def create(form=None):
    if form is None:
        form = TelegramForm()
    if form.validate_on_submit():
        return telegraph_telegram(form)
    return render_template('telegram_form.html', form=form)


@telegrams_blueprint.route('/<path:slug>', methods=['GET'])
def deliver(slug):
    telegram_dict = load_from_file_storage_or_404(slug)
    is_owner =  check_in(telegram_dict)
    return render_template('telegram.html',
                           telegram_dict=telegram_dict,
                           is_owner=is_owner,)


@telegrams_blueprint.route('/update/<slug>', methods=['GET', 'POST'])
def update(slug, form=None):
    if form is None:
        form = TelegramForm()
    telegram_dict = load_from_file_storage_or_404(slug)
    is_owner = check_in(telegram_dict)
    if not is_owner:
        abort(401)
    if form.validate_on_submit():
        return telegraph_telegram(form, slug)
    form.title.data = telegram_dict['title']
    form.signature.data = telegram_dict['signature']
    form.telegram.data = telegram_dict['telegram']
    return render_template('telegram_form.html', form=form)
