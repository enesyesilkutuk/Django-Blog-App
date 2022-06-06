let element = document.querySelector('.alert');

// setTimeout(function () {
//   element.style.display = 'none';
// }, 3000);

element &&
  setTimeout(function () {
    element.style.display = "none";
  }, 3000)