"use strict";  


  const addItemToTable = (exercise, sets, reps, 
                          repunit, weight,
                          weightunit, equipment, info) => {
      const infoPopover =
       `<a tabindex="0" class="bi bi-info-circle" role="button" data-toggle="popover" data-trigger="focus" title="${info}"  data-placement="left" data-content="test"></a>`
    $('#user-exercise-selections').append("<tr>" +
            "<td><a href='#'class='popover-anchor' data-toggle='popover'>" + exercise + "</a></td>" +
            "<td>" + sets + "</td>" +
            "<td>" + reps + "</td>" +
            "<td>" + repunit + "</td>" +
            "<td>" + weight + "</td>" +
            "<td>" + weightunit + "</td>" +
            "<td>" + equipment + "</td>" +
            "</tr>");
  

            $('.popover-anchor').popover({
              title: `${exercise}`,
              content: `<p>${info}</p>`,
              html: true
            });        
          };

  $('#exercise-form').on('submit', (evt) => {
    evt.preventDefault();
    const formInputs = {
      //'server .get requests : assign from HTML
        'api_exercise_selection': $("#api_exercise_selection").val(),
        'exercise_sets': $("#exercise_sets").val(),
        'exercise_reps': $("#exercise_reps").val(),
        'exercise_repunit': $("#exercise_repunit").val(),
        'exercise_weight': $("#exercise_weight").val(),
        'exercise_weightunit': $("#exercise_weightunit").val(),
        'api_exercise_equipment': $("#api_exercise_equipment").val() 
    }
       
    $.post("/add_exercise", formInputs, (res) => {
      
      addItemToTable(res.api_exercise_selection, 
                    res.exercise_sets, res.exercise_reps, 
                    res.exercise_repunit, res.exercise_weight, 
                    res.exercise_weightunit, 
                    res.api_exercise_equipment, res.exercise_info);
      
    });

  });

 function callPopover() {
  const elements = Array.from(document.getElementsByClassName('popover-anchor__save'));
  elements.map(element => {
    element.addEventListener('click',function() {
      const title = element.getAttribute('title');
      const content = element.getAttribute('data-content');
      const id = element.getAttribute('id');
      const id_nm = '#' + id;
        $(id_nm).popover({
              title: `${title}`,
              content: `<p>${content}</p>`,
              html: true
        });
        $(id_nm).popover("toggle");
    });
    });
 }

  window.onload = callPopover();