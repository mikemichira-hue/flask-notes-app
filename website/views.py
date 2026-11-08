from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if not note or len(note.strip()) < 1:
            flash('Note is too short.', category='error')
        else:
            new_note = Note(data=note.strip(), user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

        return redirect(url_for('views.home'))

    return render_template("home.html", user=current_user)


@views.route('/edit-note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = db.session.get(Note, note_id)

    if not note or note.user_id != current_user.id:
        flash('Note not found.', category='error')
        return redirect(url_for('views.home'))

    if request.method == 'POST':
        text = request.form.get('note')

        if not text or len(text.strip()) < 1:
            flash('Note is too short.', category='error')
        else:
            note.data = text.strip()
            db.session.commit()
            flash('Note updated!', category='success')
            return redirect(url_for('views.home'))

    return render_template("edit_note.html", note=note, user=current_user)


@views.route('/delete-note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    note = db.session.get(Note, note_id)

    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted.', category='success')

    return redirect(url_for('views.home'))