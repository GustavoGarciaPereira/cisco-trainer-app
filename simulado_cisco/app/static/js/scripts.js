// app/static/js/scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const questionContainer = document.getElementById('question-container');
    const quizForm = document.getElementById('quiz-form');
    
    // Obtenha as perguntas do template
    const questions = JSON.parse('{{ questions | tojson | safe }}');
    
    let currentQuestion = 0;
    const userAnswers = {};
    
    function showQuestion(index) {
        questionContainer.innerHTML = "";
        if (index < questions.length) {
            const q = questions[index];
            const questionDiv = document.createElement('div');
            questionDiv.className = 'question';
            questionDiv.innerHTML = `<p>${index + 1}. ${q.question}</p>`;
            
            ['option_a', 'option_b', 'option_c', 'option_d'].forEach(option => {
                const optionLabel = document.createElement('label');
                optionLabel.className = 'option';
                optionLabel.innerHTML = `
                    <input type="radio" name="q${q.id}" value="${option.slice(-1).toUpperCase()}" required>
                    ${option.slice(-1).toUpperCase()}: ${q[option]}
                `;
                questionDiv.appendChild(optionLabel);
                questionDiv.appendChild(document.createElement('br'));
            });
            
            questionContainer.appendChild(questionDiv);
        }
    }
    
    // Inicializar o primeiro questionário
    showQuestion(currentQuestion);
});
