
function load_sith_data() {


$.ajax({
        url: "/api/sith",
        type: "GET",
        success: function (data) {
            //data1 = JSON.stringify(data);
            //console.log(data['data']);
            sith_list(data['data'])
            }

    })
}

function sith_list(data) {
data.forEach(function(entry) {
    console.log(entry.name);
    let SithLi = document.createElement('a');
    SithLi.className = 'SithList';
    SithLi.setAttribute( 'href', '#')
    SithLi.setAttribute( 'id', entry.name)
    SithLi.setAttribute( 'onclick', 'get_single_sith('+ entry.id +')')
    SithLi.textContent = entry.name;
    let BrSith = document.createElement('br');
    document.querySelector('.result').appendChild(SithLi);
    document.querySelector('.result').appendChild(BrSith);
});

}

function show_recruit_form(data) {
let FormDiv = document.createElement('div');
FormDiv.className = 'recruitform';
document.querySelector('.result').appendChild(FormDiv);
let SithInputName = document.createElement('input');
SithInputName.setAttribute( 'placeholder', 'Имя')
SithInputName.setAttribute( 'id', 'Name')
let SithInputPlanet = document.createElement('select');
SithInputPlanet.className = 'select'
SithInputPlanet.setAttribute( 'id', 'Planet');
let SithInputAge = document.createElement('input');
SithInputAge.setAttribute( 'type', 'number')
SithInputAge.setAttribute( 'placeholder', 'Возраст');
SithInputAge.setAttribute( 'id', 'Age');
let SithInputEmail = document.createElement('input');
SithInputEmail.setAttribute( 'type', 'email')
SithInputEmail.setAttribute( 'placeholder', 'Email');
SithInputEmail.setAttribute( 'id', 'Email');
let SithSubmit = document.createElement('a');
SithSubmit.setAttribute( 'id', 'submit_recruiter')
SithSubmit.setAttribute( 'href', '#')
SithSubmit.setAttribute( 'onclick', 'add_recruiter()')
//
document.querySelector('.recruitform').appendChild(SithInputName);
document.querySelector('.recruitform').appendChild(SithInputAge);
document.querySelector('.recruitform').appendChild(SithInputPlanet);
document.querySelector('.recruitform').appendChild(SithInputEmail);
document.querySelector('.recruitform').appendChild(SithSubmit);


document.getElementById('submit_recruiter').text = 'Отправить';

data.forEach(function(entry) {
    console.log(entry.name);
    let RecruitOption = document.createElement('option');
    //SithLi.className = 'SithList';
    RecruitOption.textContent = entry.name;
    RecruitOption.value = entry.id;
    document.querySelector('.select').appendChild(RecruitOption);
});
}
function get_planet() {

$.ajax({
        url: "/api/planet",
        type: "GET",
        success: function (data) {
            //data1 = JSON.stringify(data);
            //console.log(data['data']);
            console.log(data);
            show_recruit_form(data['data']);
            }

    })

}
function add_recruiter() {
let name = $('#Name').val();
let planet = $('#Planet').val();
let email = $('#Email').val();
let age = parseInt($('#Age').val());
console.log(planet)
$.ajax({
        url: "/api/recruiter",
        type: "POST",
        data: ({email: email, age: parseInt(age), planet: parseInt(planet), name: name}),
        success: function (data, textStatus, xhr) {
            console.log(xhr.status)
            if (xhr.status == 200) {
            alert('Все ок!')
            questions()
            sessionStorage.setItem("email", email)
            }
            },
        error: function(data, textStatus, xhr) {

            alert('Что-то пошло не так( \nПроверьте введенные данные')
            console.log(data.status)

        }

    })


}

function questions() {

document.querySelectorAll('.recruitform').forEach(function(a){
a.remove()
})

$.ajax({
        url: "/api/questions",
        type: "GET",
        success: function (data) {
            //console.log(data['data']);
            console.log(data);
            show_questions(data['data']);
            }

    })

}
function show_questions(data) {
let QuestionsDiv = document.createElement('div');
QuestionsDiv.className = 'questionsdiv';
document.querySelector('.result').appendChild(QuestionsDiv);
data.forEach(function(entry) {
    console.log(entry.name);
    let QuLi = document.createElement('input');
    let QuLabel = document.createElement('label');
    QuLabel.setAttribute( 'id', 'label' + entry.id)

    QuLi.setAttribute( 'type', 'checkbox')
    QuLi.setAttribute( 'id', entry.id)
    //QuLi.setAttribute( 'checked', 'checked')
    QuLabel.setAttribute( 'for', entry.id)

    QuLi.className = 'QuList';
    document.querySelector('.questionsdiv').appendChild(QuLi);
    document.querySelector('.questionsdiv').appendChild(QuLabel);
    document.getElementById('label'+ entry.id).innerText = entry.name;


});
    let AnswerSubmit = document.createElement('a');
    AnswerSubmit.setAttribute( 'id', 'submit_answer')
    AnswerSubmit.setAttribute( 'href', '#')
    AnswerSubmit.setAttribute( 'onclick', 'add_answer()');
    document.querySelector('.questionsdiv').appendChild(AnswerSubmit);
    document.getElementById('submit_answer').text = 'Отправить';

}
function add_answer() {
let checkbox_value = document.getElementsByClassName('QuList');
//console.log(checkbox_value);
let arr_check = [];
let arr_id = []
for(let e of checkbox_value) {
arr_check.push(e.checked);
arr_id.push(e.id)
}
add_answer_api(arr_check, arr_id);
}

function add_answer_api(data, id) {
console.log(data)
email = sessionStorage.getItem("email")

$.ajax({
        url: "/api/answer",
        type: "POST",
        data: ({email: email, answer: data, questions: id}),
        success: function (data, textStatus, xhr) {
        if (xhr.status == 200) {
            alert('Спасибо за ответы!');
            document.querySelectorAll('.questionsdiv').forEach(function(a){
            a.remove()
})
            }

            //console.log(data['data']);

            }

    })

}
function get_single_sith(data1) {

$.ajax({
        url: "/api/single_sith/",
        type: "GET",
        data: ({sith: data1 }),
        success: function (data) {
            //console.log(data['data']);
            console.log(data);
            document.querySelectorAll('.SithList').forEach(function(a){
            a.remove()})
            show_recruit(data['recruit']);
            sessionStorage.setItem("sith", data1)


            }

    })
}

function show_recruit(data) {
console.log(data)
data.forEach(function(entry) {
    console.log(entry.name);
    let SithLi = document.createElement('a');
    let EnrollA = document.createElement('a');
    let EnrollBr = document.createElement('br');
    EnrollA.setAttribute('href', '#');
    EnrollA.textContent = ' Зачислить в Руки Тени';
    EnrollA.setAttribute('onclick', 'enroll(' + entry.id + ')')
    SithLi.className = 'SithList';
    SithLi.setAttribute( 'href', '#')
    //SithLi.setAttribute( 'onclick', 'get_single_sith('+ entry.id +')')
    SithLi.textContent = entry.name;
    console.log(entry.answer)
    document.querySelector('.result').appendChild(SithLi);
    document.querySelector('.result').appendChild(EnrollBr);
    document.querySelector('.result').appendChild(EnrollA);
    //document.querySelector('.result').appendChild(BrSith);
    entry.answer.forEach(function(e){
    console.log(e.result)
    let SithP1 = document.createElement('p');
    let SithP2 = document.createElement('p');
    SithP1.className = 'SithP1'
    SithP2.className = 'SithP2'
    SithP1.setAttribute('id', e.questions.id)
    //SithP2.setAttribute('id', e.questions.id)

    SithP2.textContent = e.questions.name;
    document.querySelector('.result').appendChild(SithP2);
    document.querySelector('.result').appendChild(SithP1);

    document.getElementById(e.questions.id).innerText = e.result;
    let H1rec = document.createElement('hr');
    document.querySelector('.result').appendChild(H1rec);

    })

    //let BrSith = document.createElement('br');


});


}
function enroll(data) {
console.log(data)
id = data
sith = sessionStorage.getItem("sith")
$.ajax({
        url: "/api/enroll",
        type: "POST",
        data: ({recruit: id, sith: sith }),
        success: function (data, textStatus, xhr) {
        if (xhr.status == 200) {
            alert('Рекрут зачислен!');
//            document.querySelectorAll('.questionsdiv').forEach(function(a){
//            a.remove()
//})
            }

            //console.log(data['data']);

            }

    })

}