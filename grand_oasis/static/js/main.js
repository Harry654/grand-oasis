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







let price_per_night = 0;
function setRoom () {
    let newRoomID = event.target.getAttribute('room_id');
    let newRoomNumber = event.target.getAttribute('room_number');
    let newRoomType = event.target.getAttribute('room_category');
    let new_price_per_night = parseInt(event.target.getAttribute('price_per_night'));
    
    document.getElementById("myForm").reset();
    amount.innerHTML = 'Amount: $0';
    duration.innerHTML = 'Duration: 0 days';
    
    document.getElementById("room_number").innerHTML = `Room Number: ${newRoomNumber}`;
    document.getElementById("room_type").innerHTML = `Room Type: ${newRoomType}`;
    document.getElementById("room").value = newRoomID;
    price_per_night = new_price_per_night;
};

function setDetails() {
    let roomCategory = event.target.getAttribute('room_category');
    document.getElementById("detailModalLabel").innerHTML = roomCategory;
    
    if(roomCategory === 'Junior Suite') {
        // document.getElementById("detailsImg").setAttribute("src", "{% static 'img/room-1.jpg' %}");
        document.getElementById("detailsDesc").innerHTML = "Step into our comfortable and affordable basic hotel room, designed with your convenience in mind. Unwind in a cozy and inviting atmosphere, complete with a well-appointed en-suite bathroom and a snug bed that guarantees a restful night's sleep. Stay productive with a dedicated workspace, ideal for catching up on work or planning your itinerary. Whether you're a budget-conscious traveler or simply seeking simplicity, our basic hotel room provides all the essentials for a pleasant stay without compromising on comfort.";
        document.getElementById("detailsPrice").innerHTML = "$120 / Night";

    }
    
    if(roomCategory === 'Executive Suite') {
        // document.getElementById("detailsImg").setAttribute("src", "{% static 'img/room-1.jpg' %}");
        document.getElementById("detailsDesc").innerHTML = "Indulge in a delightful experience in our standard hotel room, where modern elegance and comfort seamlessly come together. Immerse yourself in the tastefully designed space, featuring stylish décor and thoughtful amenities. Drift into tranquility on the comfortable bed, and refresh in the well-appointed bathroom that offers both functionality and style. Whether you're traveling for business or leisure, our standard room provides the perfect retreat to relax and recharge after a day of exploring. Embrace the balance of comfort, convenience, and affordability in our inviting standard hotel room.";
        document.getElementById("detailsPrice").innerHTML = "$300 / Night";

    }
    
    if(roomCategory === 'Super Deluxe') {
        // document.getElementById("detailsImg").setAttribute("src", "{% static 'img/room-1.jpg' %}");
        document.getElementById("detailsDesc").innerHTML = "Experience the epitome of luxury and sophistication in our executive hotel room. From the moment you step inside, you'll be enveloped in an ambiance of elegance and refinement. Indulge in the spaciousness of the room, carefully adorned with upscale furnishings and captivating décor. Sink into the plush king-size bed and revel in its comfort. The upgraded bathroom offers a touch of opulence, featuring premium fixtures and luxurious amenities. As an executive guest, you'll enjoy exclusive access to our executive lounge, where personalized services and complimentary perks await. Whether you're traveling for business or seeking a luxurious retreat, our executive room exceeds expectations, offering an extraordinary stay tailored to the discerning traveler.";
        document.getElementById("detailsPrice").innerHTML = "$500 / Night";

    }

}
 

let checkin = document.getElementById("checkin");
let checkout = document.getElementById("checkout");
let duration = document.getElementById("duration");
let amount = document.getElementById("amount");

checkin.addEventListener("input", () => {calculateAmount(price_per_night)});

checkout.addEventListener("input", () => {calculateAmount(price_per_night)});

function calculateAmount(price_per_night = price_per_night) {
    let daysDiff = calculateDateDifference(checkin, checkout, duration);
    if (daysDiff) amount.innerHTML = `Amount: $${daysDiff * price_per_night}`;
    else amount.innerHTML = `Amount: $${0}`;
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
