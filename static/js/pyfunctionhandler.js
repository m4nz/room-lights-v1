$("#on").click(function(){
    $.ajax({
      type: 'GET',
      url: "/turnonlights",
      data: "",
      dataType: "text",
      success: console.log("Lights on")
    });
});

$("#off").click(function(){
    $.ajax({
      type: 'GET',
      url: "/turnofflights",
      data: "",
      dataType: "text",
      success: console.log("Lights off")
    });
});
$("#update").click(function(){
  var temp = $('#selectedeffect').val();
  var effect = String(temp)
    $.ajax({
      type: 'GET',
      url: "/seteffect",
      data: {r1: r1, g1: g1, b1: b1, r2: r2, g2: g2, b2: b2, effect: effect},
      dataType: "text",
      success: console.log("Led strip color updated")
    });
});
