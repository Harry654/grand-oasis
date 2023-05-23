let price_per_night = 0;
console.log("🚀 ~ file: main.js:109 ~ price_per_night:", price_per_night)
function setRoom() {
  let newRoomID = event.target.getAttribute("room_id");
  
  document.getElementById(`myForm${newRoomID}`).reset();
  document.getElementById(`amount${newRoomID}`).innerHTML = "Amount: $0";
  document.getElementById(`duration${newRoomID}`).innerHTML = "Duration: 0 days";
  
  let new_price_per_night = parseInt(
    event.target.getAttribute("price_per_night")
  );
  price_per_night = new_price_per_night;
}

let checkin = document.getElementsByClassName("checkin");
let checkout = document.getElementsByClassName("checkout");
let duration = document.getElementsByClassName("duration");
let amount = document.getElementsByClassName("amount");

for (let i = 0; i < checkin.length; i++) {
  checkin[i].addEventListener("input", () => {
    calculateAmount(i, price_per_night);
  });
  checkout[i].addEventListener("input", () => {
    calculateAmount(i, price_per_night);
  });
}

function calculateAmount(index, price_per_night = price_per_night) {
  let daysDiff = calculateDateDifference(
    checkin[index],
    checkout[index],
    duration[index]
  );
  if (daysDiff)
    amount[index].innerHTML = `Amount: $${daysDiff * price_per_night}`;
  else amount[index].innerHTML = `Amount: $${0}`;
}

function calculateDateDifference(start_date_param, end_date_param, duration) {
  let start_date = new Date(start_date_param.value);
  let end_date = new Date(end_date_param.value);

  // Calculate the time difference in milliseconds
  let timeDiff = end_date - start_date;

  if (timeDiff <= 0) {
    alert("Invalid date range");
    duration.innerHTML = `Duration: ${0} days`;
    end_date_param.value = start_date_param.value;
    return false;
  }

  if (isNaN(timeDiff)) return false;

  // Convert the time difference to days
  let daysDiff = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));

  duration.innerHTML = `Duration: ${daysDiff} days`;

  return daysDiff;
}


(function ($) {
  "use strict";

  // Spinner
  var spinner = function () {
    setTimeout(function () {
      if ($("#spinner").length > 0) {
        $("#spinner").removeClass("show");
      }
    }, 1);
  };
  spinner();

  // Initiate the wowjs
  new WOW().init();

  // Dropdown on mouse hover
  const $dropdown = $(".dropdown");
  const $dropdownToggle = $(".dropdown-toggle");
  const $dropdownMenu = $(".dropdown-menu");
  const showClass = "show";

  $(window).on("load resize", function () {
    if (this.matchMedia("(min-width: 992px)").matches) {
      $dropdown.hover(
        function () {
          const $this = $(this);
          $this.addClass(showClass);
          $this.find($dropdownToggle).attr("aria-expanded", "true");
          $this.find($dropdownMenu).addClass(showClass);
        },
        function () {
          const $this = $(this);
          $this.removeClass(showClass);
          $this.find($dropdownToggle).attr("aria-expanded", "false");
          $this.find($dropdownMenu).removeClass(showClass);
        }
      );
    } else {
      $dropdown.off("mouseenter mouseleave");
    }
  });

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
      $(".back-to-top").fadeIn("slow");
    } else {
      $(".back-to-top").fadeOut("slow");
    }
  });
  $(".back-to-top").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1500, "easeInOutExpo");
    return false;
  });

  // Facts counter
  $('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 2000,
  });

  // Modal Video
  $(document).ready(function () {
    var $videoSrc;
    $(".btn-play").click(function () {
      $videoSrc = $(this).data("src");
    });
    console.log($videoSrc);

    $("#videoModal").on("shown.bs.modal", function (e) {
      $("#video").attr(
        "src",
        $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0"
      );
    });

    $("#videoModal").on("hide.bs.modal", function (e) {
      $("#video").attr("src", $videoSrc);
    });
  });

  // Testimonials carousel
  $(".testimonial-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1000,
    margin: 25,
    dots: false,
    loop: true,
    nav: true,
    navText: [
      '<i class="bi bi-arrow-left"></i>',
      '<i class="bi bi-arrow-right"></i>',
    ],
    responsive: {
      0: {
        items: 1,
      },
      768: {
        items: 2,
      },
    },
  });
})(jQuery);
