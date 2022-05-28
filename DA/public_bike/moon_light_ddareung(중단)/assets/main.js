const togglebtn = document.querySelector('.test_start');
const target = document.querySelector('.test_target');

togglebtn.addEventListener('click', ()=> {
    target.classList.toggle('active');
});