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

function setRoomNumber(newRoomNumber, type) {
    if(type === 'js') document.getElementById("js_room_number").innerHTML = `Room Number: ${newRoomNumber}`;
    if(type === 'es') document.getElementById("es_room_number").innerHTML = `Room Number: ${newRoomNumber}`;
    if(type === 'sd') document.getElementById("sd_room_number").innerHTML = `Room Number: ${newRoomNumber}`;
}

let js_checkin = document.getElementById("js_checkin");
let js_checkout = document.getElementById("js_checkout");
let js_duration = document.getElementById("js_duration");
let js_amount = document.getElementById("js_amount");
const js_price_per_night = 120;

let es_checkin = document.getElementById("es_checkin");
let es_checkout = document.getElementById("es_checkout");
let es_duration = document.getElementById("es_duration");
let es_amount = document.getElementById("es_amount");
const es_price_per_night = 300;

let sd_checkin = document.getElementById("sd_checkin");
let sd_checkout = document.getElementById("sd_checkout");
let sd_duration = document.getElementById("sd_duration");
let sd_amount = document.getElementById("sd_amount");
const sd_price_per_night = 500;

js_checkin.addEventListener("input", function (event) {
  let daysDiff = calculateDateDifference(js_checkin, js_checkout, js_duration);
  if (daysDiff) js_amount.innerHTML = `Amount: $${daysDiff * js_price_per_night}`;
  else js_amount.innerHTML = `Amount: $${0}`;
});

js_checkout.addEventListener("input", function (event) {
  let daysDiff = calculateDateDifference(js_checkin, js_checkout, js_duration);
  if (daysDiff) js_amount.innerHTML = `Amount: $${daysDiff * js_price_per_night}`;
  else js_amount.innerHTML = `Amount: $${0}`;
});

es_checkin.addEventListener("input", function (event) {
  let daysDiff = calculateDateDifference(es_checkin, es_checkout, es_duration);
  if (daysDiff) es_amount.innerHTML = `Amount: $${daysDiff * es_price_per_night}`;
  else es_amount.innerHTML = `Amount: $${0}`;
});

es_checkout.addEventListener("input", function (event) {
  let daysDiff = calculateDateDifference(es_checkin, es_checkout, es_duration);
  if (daysDiff) es_amount.innerHTML = `Amount: $${daysDiff * es_price_per_night}`;
  else es_amount.innerHTML = `Amount: $${0}`;
});

sd_checkin.addEventListener("input", function (event) {
  let daysDiff = calculateDateDifference(sd_checkin, sd_checkout, sd_duration);
  if (daysDiff) sd_amount.innerHTML = `Amount: $${daysDiff * sd_price_per_night}`;
  else sd_amount.innerHTML = `Amount: $${0}`;
});

sd_checkout.addEventListener("input", function (event) {
  let daysDiff = calculateDateDifference(sd_checkin, sd_checkout, sd_duration);
  if (daysDiff) sd_amount.innerHTML = `Amount: $${daysDiff * sd_price_per_night}`;
  else sd_amount.innerHTML = `Amount: $${0}`;
});

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
