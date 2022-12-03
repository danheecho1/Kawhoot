let title = document.getElementById("title");
let description = document.getElementById("description");

let max = 255;
let remaining_characters = document.getElementById("remaining_characters")
remaining_characters.textContent = max - description.value.length;

description.addEventListener('input', function() {
    remaining_characters.textContent = max - this.value.length;
})

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

next0.onclick = function() {
    if(title.value && description.value) {
        question0.style.display = "none";
        question1.style.display = 'block';
    }
    else {
        alert("All fields must be filled in!")
    }
}

next1.onclick = function() {
    if(prompt1.value && a1.value && b1.value && c1.value && d1.value && e1.value) {
        question1.style.display = "none";
        question2.style.display = 'block';
    }
    else {
        alert("All fields must be filled in!")
    }
}

back1.onclick = function() {
    question1.style.display = "none";
    question0.style.display = 'block';
}

next2.onclick = function() {
    if(prompt2.value && a2.value && b2.value && c2.value && d2.value && e2.value) {
    question2.style.display = 'none';
    question3.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back2.onclick = function() {
    question2.style.display = 'none';
    question1.style.display = 'block';
}

next3.onclick = function() {
    if(prompt3.value && a3.value && b3.value && c3.value && d3.value && e3.value) {
    question3.style.display = 'none';
    question4.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back3.onclick = function() {
    question3.style.display = 'none';
    question2.style.display = 'block';
}

next4.onclick = function() {
    if(prompt4.value && a4.value && b4.value && c4.value && d4.value && e4.value) {
    question4.style.display = 'none';
    question5.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back4.onclick = function() {
    question4.style.display = 'none';
    question3.style.display = 'block';
}

next5.onclick = function() {
    if(prompt5.value && a5.value && b5.value && c5.value && d5.value && e5.value) {
    question5.style.display = 'none';
    question6.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back5.onclick = function() {
    question5.style.display = 'none';
    question4.style.display = 'block';
}

next6.onclick = function() {
    if(prompt6.value && a6.value && b6.value && c6.value && d6.value && e6.value) {
    question6.style.display = 'none';
    question7.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back6.onclick = function() {
    question6.style.display = 'none';
    question5.style.display = 'block';
}

next7.onclick = function() {
    if(prompt7.value && a7.value && b7.value && c7.value && d7.value && e7.value) {
    question7.style.display = 'none';
    question8.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back7.onclick = function() {
    question7.style.display = 'none';
    question6.style.display = 'block';
}

next8.onclick = function() {
    if(prompt8.value && a8.value && b8.value && c8.value && d8.value && e8.value) {
    question8.style.display = 'none';
    question9.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back8.onclick = function() {
    question8.style.display = 'none';
    question7.style.display = 'block';
}

next9.onclick = function() {
    if(prompt9.value && a9.value && b9.value && c9.value && d9.value && e9.value) {
    question9.style.display = 'none';
    question10.style.display = 'block';
    }
    else {
    alert("All fields must be filled in!")
    }
}

back9.onclick = function() {
    question9.style.display = 'none';
    question8.style.display = 'block';
}

next10.onclick = function() {
    if(!prompt10.value || !a10.value || !b10.value || !c10.value || !d10.value || !e10.value) {
        alert("All fields must be filled in!")
        next10.setAttribute('type', 'button')
        }
    else if (prompt10.value && a10.value && b10.value && c10.value && d10.value && e10.value) {
        next10.setAttribute('type', 'submit')
    }
}

back10.onclick = function() {
    question10.style.display = 'none';
    question9.style.display = 'block';
}