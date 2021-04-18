"use strict";

  const addItemToTable = (exercise, sets, reps, repunit, info) => {
    $('#user-exercise-selections').append("<tr>" +
            "<td>" + exercise + "</td>" +
            "<td>" + sets + "</td>" +
            "<td>" + reps + "</td>" +
            "<td>" + repunit + "</td>" +
            "<td>" + info + "</td>" +
            "</tr>");
  };


  $('#exercise-form').on('submit', (evt) => {
    evt.preventDefault();
    const formInputs = {
      //'server .get requests : assign from HTML
        'exercise_selection': $("#exercise_name").val(),
        'exercise_sets': $("#exercise_sets").val(),
        'exercise_reps': $("#exercise_reps").val(),
        'exercise_repunit': $("#exercise_repunit").val() 
    }

    $.post("/add_exercise", formInputs, (res) => {
      console.log(res.exercise_info);
      addItemToTable(res.exercise_selection, 
                    res.exercise_sets, res.exercise_reps, 
                    res.exercise_repunit, res.exercise_info);
      // alert('workout successfully added!');
    })
  });



  //do I  need function to reset
  //form for user to pick new exercises??
  //
  //need to figure out how to get the correct variable 
  //in add item
