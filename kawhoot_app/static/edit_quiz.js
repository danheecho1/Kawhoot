var correct_answer_1 = document.getElementById("correct_answer_1").value
var correct_option_1 = document.getElementById(`select1${correct_answer_1}`)
correct_option_1.setAttribute("selected", "selected")

var correct_answer_2 = document.getElementById("correct_answer_2").value
var correct_option_2 = document.getElementById(`select2${correct_answer_2}`)
correct_option_2.setAttribute("selected", "selected")

var correct_answer_3 = document.getElementById("correct_answer_3").value
var correct_option_3 = document.getElementById(`select3${correct_answer_3}`)
correct_option_3.setAttribute("selected", "selected")

var correct_answer_4 = document.getElementById("correct_answer_4").value
var correct_option_4 = document.getElementById(`select4${correct_answer_4}`)
correct_option_4.setAttribute("selected", "selected")

var correct_answer_5 = document.getElementById("correct_answer_5").value
var correct_option_5 = document.getElementById(`select5${correct_answer_5}`)
correct_option_5.setAttribute("selected", "selected")

var correct_answer_6 = document.getElementById("correct_answer_6").value
var correct_option_6 = document.getElementById(`select6${correct_answer_6}`)
correct_option_6.setAttribute("selected", "selected")

var correct_answer_7 = document.getElementById("correct_answer_7").value
var correct_option_7 = document.getElementById(`select7${correct_answer_7}`)
correct_option_7.setAttribute("selected", "selected")

var correct_answer_8 = document.getElementById("correct_answer_8").value
var correct_option_8 = document.getElementById(`select8${correct_answer_8}`)
correct_option_8.setAttribute("selected", "selected")

var correct_answer_9 = document.getElementById("correct_answer_9").value
var correct_option_9 = document.getElementById(`select9${correct_answer_9}`)
correct_option_9.setAttribute("selected", "selected")

var correct_answer_10 = document.getElementById("correct_answer_10").value
var correct_option_10 = document.getElementById(`select10${correct_answer_10}`)
correct_option_10.setAttribute("selected", "selected")

var max = 255;
var remaining_characters = document.getElementById("remaining_characters")

remaining_characters.textContent = max - description.value.length;

description.addEventListener('input', function() {
    remaining_characters.textContent = max - this.value.length;
})  