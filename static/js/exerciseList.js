"use strict";

const addItemToTable = (itemName) => {
    $('#user-exercise-selections').append(`
      <tr>
        <td>${itemName}</td>
      </tr>
    `);
  };

  //going to need function to reset
  //form for user to pick new exercises
  //
  //need to figure out how to get the correct variable 
  //in add item

  $('#submit-exercise').on('click', () => {
    addItemToTable('');
  });


  function tableUpdate() {
        
    addExerciseToTable();

    formClear();

}



  function productAddToTable() {
    // First check if a <tbody> tag exists, add one if not
    if ($("#productTable tbody").length == 0) {
        $("#productTable").append("<tbody></tbody>");
    }

    // Append product to the table
    $("#productTable tbody").append("<tr>" +
        "<td>" + $("#productname").val() + "</td>" +
        "<td>" + $("#introdate").val() + "</td>" +
        "<td>" + $("#url").val() + "</td>" +
        "</tr>");
}





