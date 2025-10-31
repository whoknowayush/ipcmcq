from django.shortcuts import render, redirect
from .models import Question, Option
import random

def quiz_view(request):
    all_qs = list(Question.objects.prefetch_related('options').all())
    random.shuffle(all_qs)
    questions = all_qs[:10]  # take up to 10
    num_questions = len(questions)
    # Pass questions and the number (for scoring)
    return render(request, 'exam/quiz.html', {'questions': questions, 'num_questions': num_questions})


def submit_quiz(request):
    if request.method != 'POST':
        return redirect('quiz')

    # Determine number of questions used (so we can show e.g., 8/10 if less available)
    # The frontend will include hidden input 'num_questions' so trust that value
    try:
        num_questions = int(request.POST.get('num_questions', 0))
    except:
        num_questions = 0

    correct = 0
    # For each question the form sends 'question_<id>' => option_id (string)
    for key, value in request.POST.items():
        if not key.startswith('question_'):
            continue
        qid = key.split('_', 1)[1]
        try:
            # ensure option belongs to that question
            opt_id = int(value)
            option = Option.objects.get(id=opt_id, question_id=qid)
            if option.is_correct:
                correct += 1
        except Exception:
            # ignore invalid/missing selections
            pass

    score = correct
    total = num_questions
    return render(request, 'exam/result.html', {'score': score, 'total': total})


def auto_submit_exam(request):
    if request.method == "POST":
        # 🔹 Logic to automatically submit the user's exam
        # Example:
        # current_exam = Exam.objects.get(user=request.user, status='in_progress')
        # current_exam.status = 'submitted'
        # current_exam.submission_reason = 'Tab switch violation'
        # current_exam.save()

        print("Auto submission triggered due to tab switch!")
        return JsonResponse({"status": "submitted"})
    return JsonResponse({"error": "Invalid request"}, status=400)


def exam_submitted(request):
    return render(request, "exam_submitted.html")
