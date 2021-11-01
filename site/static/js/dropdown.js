document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var options = {
        coverTrigger: false,
    }
    var instances = M.Dropdown.init(elems, options);
  });