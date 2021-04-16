"use strict";

  const addItemToTable = (exercise, sets, reps) => {
    $('#user-exercise-selections').append("<tr>" +
            "<td>" + exercise + "</td>" +
            "<td>" + sets + "</td>" +
            "<td>" + reps + "</td>" +
            "</tr>");
  };


  $('#exercise-form').on('submit', (evt) => {
    evt.preventDefault();
    const formInputs = {
      //'server .get requests : assign from HTML
        'exercise_selection': $("#exercise_name").val(),
        'exercise_sets': $("#exercise_sets").val(),
        'exercise_reps': $("#exercise_reps").val()
    }

    $.post("/add_exercise", formInputs, (res) => {
      console.log(res);
      addItemToTable(res.exercise_selection, res.exercise_sets, res.exercise_reps);
      alert('workout successfully added!');
    })
  });



  //do I  need function to reset
  //form for user to pick new exercises??
  //
  //need to figure out how to get the correct variable 
  //in add item
