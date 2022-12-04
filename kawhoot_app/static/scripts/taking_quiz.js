for(let i = 0; i < 11; i++) {
    window['question' + i] = document.getElementById('question' + i);
    window['next' + i] = document.getElementById('next' + i);
    window['back' + i] = document.getElementById('back' + i);
    window['prompt' + i] = document.getElementById('prompt' + i);
    window['a' + i] = document.getElementById(i + 'a');
    window['b' + i] = document.getElementById(i + 'b');
    window['c' + i] = document.getElementById(i + 'c');
    window['d' + i] = document.getElementById(i + 'd');
    window['e' + i] = document.getElementById(i + 'e');
}

let question1 = document.getElementById("question1_attempt")

next1.onclick = function() {
    question1_attempt.style.display = "none";
    question2.style.display = 'block';
}

next2.onclick = function() {
    question2.style.display = 'none';
    question3.style.display = 'block';
}

back2.onclick = function() {
    question2.style.display = 'none';
    question1_attempt.style.display = 'block';
}

next3.onclick = function() {
    question3.style.display = 'none';
    question4.style.display = 'block';
}

back3.onclick = function() {
    question3.style.display = 'none';
    question2.style.display = 'block';
}

next4.onclick = function() {
    question4.style.display = 'none';
    question5.style.display = 'block';
}

back4.onclick = function() {
    question4.style.display = 'none';
    question3.style.display = 'block';
}

next5.onclick = function() {
    question5.style.display = 'none';
    question6.style.display = 'block';
}

back5.onclick = function() {
    question5.style.display = 'none';
    question4.style.display = 'block';
}

next6.onclick = function() {
    question6.style.display = 'none';
    question7.style.display = 'block';
}

back6.onclick = function() {
    question6.style.display = 'none';
    question5.style.display = 'block';
}

next7.onclick = function() {
    question7.style.display = 'none';
    question8.style.display = 'block';
}

back7.onclick = function() {
    question7.style.display = 'none';
    question6.style.display = 'block';
}

next8.onclick = function() {
    question8.style.display = 'none';
    question9.style.display = 'block';
}

back8.onclick = function() {
    question8.style.display = 'none';
    question7.style.display = 'block';
}

next9.onclick = function() {
    question9.style.display = 'none';
    question10.style.display = 'block';
}

back9.onclick = function() {
    question9.style.display = 'none';
    question8.style.display = 'block';
}

next10.onclick = function() {
    let answer1 = document.querySelector('input[name="answer1"]:checked');
    let answer2 = document.querySelector('input[name="answer2"]:checked');
    let answer3 = document.querySelector('input[name="answer3"]:checked');
    let answer4 = document.querySelector('input[name="answer4"]:checked');
    let answer5 = document.querySelector('input[name="answer5"]:checked');
    let answer6 = document.querySelector('input[name="answer6"]:checked');
    let answer7 = document.querySelector('input[name="answer7"]:checked');
    let answer8 = document.querySelector('input[name="answer8"]:checked');
    let answer9 = document.querySelector('input[name="answer9"]:checked');
    let answer10 = document.querySelector('input[name="answer10"]:checked');
    if(!answer1 || !answer2 || !answer3 || !answer4 || !answer5 || !answer6 || !answer7 || !answer8 || !answer9 || !answer10) {
        next10.setAttribute('type', 'button')
        alert("All questions must be answered!")
        }
    else {
        next10.setAttribute('type', 'submit')
    }
}

back10.onclick = function() {
    question10.style.display = 'none';
    question9.style.display = 'block';
}