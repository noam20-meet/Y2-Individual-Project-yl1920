var board2 = Chessboard('board2', {
  draggable: true,
  dropOffBoard: 'trash',
  sparePieces: true
})

$('#startBtn').on('click', board2.start)
$('#clearBtn').on('click', board2.clear)


  var displayTime, resetButtonClasses;

    function getTimeString(time) {
    var secs;
    secs = time.get('seconds');
    if (secs < 10) {
      secs = `0${secs}`;
    }
    return `${time.get('minutes')}:${secs}`;
  };

    function resetButtonClasses  () {
    $("#left input").addClass("btn-primary");
    $("#left input").removeClass("btn-default btn-disabled");
    $("#right input").addClass("btn-primary");
    return $("#right input").removeClass("btn-default btn-disabled");
  };



  displayTime = function (elem, time) {
    return $(elem).html(getTimeString(time));
  };



  jQuery(function ($) {
    var leftTimer, resetAll, rightTimer, t1, t2;
    t1 = moment.duration(20, "minutes");
    t2 = moment.duration(20, "minutes");
    displayTime("#left .time", t1);
    displayTime("#right .time", t2);


    rightTimer = $('#right .toggle').on('click', function () {


      if (leftTimer) {
        clearInterval(leftTimer);
        toggleButtons("right");
      }
      return rightTimer = setInterval(function () {
        if (t2.as('seconds') > 0) {
          t2.subtract(moment.duration(1, 's'));
          return displayTime("#right .time", t2);
        } else {
          return clearInterval(self);
        }
      }, 1000);
    });


    leftTimer = $('#left .toggle').on('click', function () {
      if (rightTimer) {
        clearInterval(rightTimer);
        toggleButtons("left");
      }
      return leftTimer = setInterval(function () {
        if (t1.as('seconds') > 0) {
          t1.subtract(moment.duration(1, 's'));
          return displayTime("#left .time", t1);
        } else {
          return clearInterval(self);
        }
      }, 1000);
    });

    $("#pause").on('click', function () {
      if ($("#left .toggle").prop === "disabled") {
        toggleButtons("left");
      } else {
        toggleButtons("right");
      }
      clearInterval(leftTimer);
      return clearInterval(rightTimer);
    });


    $("#reset").on('click', function () {
      $('#time-input').val(20);
      return resetAll(20);
    });
    $('#time-input').on('change', function () {
      return resetAll(parseInt($('#time-input').val()));
    });
    return resetAll = function (minutes) {
      clearInterval(leftTimer);
      clearInterval(rightTimer);
      t1 = moment.duration(minutes, "minutes");
      t2 = moment.duration(minutes, "minutes");
      displayTime("#left .time", t1);
      displayTime("#right .time", t2);

   
      $("#left input").prop("disabled", false);
      $("#right input").prop("disabled", false);

      
      return resetButtonClasses();
    };
  });

s