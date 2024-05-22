(function () {
  // INITIALIZATION OF MEGA MENU
  // =======================================================
  new HSMegaMenu(".js-mega-menu", {
    desktop: {
      position: "left"
    }
  });

  // INITIALIZATION OF SHOW ANIMATIONS
  // =======================================================
  new HSShowAnimation(".js-animation-link");

  // INITIALIZATION OF BOOTSTRAP VALIDATION
  // =======================================================
  HSBsValidation.init(".js-validate", {
    onSubmit: (data) => {
      data.event.preventDefault();
      alert("Submited");
    }
  });

  // INITIALIZATION OF BOOTSTRAP DROPDOWN
  // =======================================================
  HSBsDropdown.init();

  // INITIALIZATION OF GO TO
  // =======================================================
  new HSGoTo(".js-go-to");

  // INITIALIZATION OF SWIPER
  // =======================================================
  var sliderThumbs = new Swiper(".js-swiper-shop-hero-thumbs", {
    watchSlidesVisibility: true,
    watchSlidesProgress: true,
    history: false,
    slidesPerView: 3,
    spaceBetween: 15,
    on: {
      beforeInit: (swiper) => {
        const css = `.swiper-slide-thumb-active .swiper-thumb-progress .swiper-thumb-progress-path {
                opacity: 1;
                -webkit-animation: ${swiper.originalParams.autoplay.delay}ms linear 0ms forwards swiperThumbProgressDash;
                animation: ${swiper.originalParams.autoplay.delay}ms linear 0ms forwards swiperThumbProgressDash;
            }`;
        style = document.createElement("style");
        document.head.appendChild(style);
        style.type = "text/css";
        style.appendChild(document.createTextNode(css));

        swiper.el
          .querySelectorAll(".js-swiper-thumb-progress")
          .forEach((slide) => {
            slide.insertAdjacentHTML(
              "beforeend",
              '<span class="swiper-thumb-progress"><svg version="1.1" viewBox="0 0 160 160"><path class="swiper-thumb-progress-path" d="M 79.98452083651917 4.000001576345426 A 76 76 0 1 1 79.89443752470656 4.0000733121155605 Z"></path></svg></span>'
            );
          });
      }
    }
  });

  var swiper = new Swiper(".js-swiper-shop-classic-hero", {
    autoplay: true,
    loop: true,
    navigation: {
      nextEl: ".js-swiper-shop-classic-hero-button-next",
      prevEl: ".js-swiper-shop-classic-hero-button-prev"
    },
    thumbs: {
      swiper: sliderThumbs
    }
  });

  // INITIALIZATION OF COUNTDOWN
  // =======================================================
  const oneYearFromNow = new Date();

  document.querySelectorAll(".js-countdown").forEach((item) => {
    const days = item.querySelector(".js-cd-days"),
      hours = item.querySelector(".js-cd-hours"),
      minutes = item.querySelector(".js-cd-minutes"),
      seconds = item.querySelector(".js-cd-seconds");

    countdown(
      oneYearFromNow.setFullYear(oneYearFromNow.getFullYear() + 1),
      (ts) => {
        days.innerHTML = ts.days;
        hours.innerHTML = ts.hours;
        minutes.innerHTML = ts.minutes;
        seconds.innerHTML = ts.seconds;
      },
      countdown.DAYS | countdown.HOURS | countdown.MINUTES | countdown.SECONDS
    );
  });
})();

function pageChange(pageNumber) {
  let urlParam = new URLSearchParams(window.location.search);
  urlParam.set("page", pageNumber);
  let new_url = window.location.pathname + "?" + urlParam.toString();
  window.location.href = new_url;
}

function formatPriceInToman(element) {
  let rawPrice = parseFloat(element.innerText);
  let formatter = new Intl.NumberFormat("fa-IR");
  let formattedPrice = formatter.format(rawPrice);
  element.innerText = `${formattedPrice} تومان`;
}

document.addEventListener("DOMContentLoaded", function () {
  let priceElements = document.querySelectorAll(".formatted-price");
  priceElements.forEach((element) => formatPriceInToman(element));
});

function addToCart(productId) {
  const url = $("#add-to-cart").attr("data-url");
  // const csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();  //! this for {% csrf_token %} cause input
  const csrfmiddlewaretoken = $("#add-to-cart").attr("data-csrf");

  $.ajax({
    method: "POST",
    url: url,
    data: {
      product_id: productId,
      csrfmiddlewaretoken: csrfmiddlewaretoken
    },
    success(response) {
      console.log(response.total_quantity);
      $("#total-cart-item-count").html(response.total_quantity);
      // do something with the response data
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log(errorThrown);
      // handle the error case
    }
  });
}

function updateCartQuantity(productId, quantity) {
  const url = $("#cart-update-quantity").data("url");
  const csrfmiddlewaretoken = $("#cart-update-quantity").data("csrf");
  console.log(url, csrfmiddlewaretoken);
  $.ajax({
    url: url,
    method: "POST",

    data: {
      product_id: productId,
      quantity: quantity,
      csrfmiddlewaretoken: csrfmiddlewaretoken
    },
    success: function (response) {
      console.log(response);
      location.reload();
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log(errorThrown);
      // handle the error case
    }
  });
}

function removeCartItem(productID) {
  const url = $("#remove-cart-item").data("url");
  const csrfmiddlewaretoken = $("#remove-cart-item").data("csrf");
  console.log(url , csrfmiddlewaretoken)
  $.ajax({
    method: "POST",
    url: url,
    data: {
      product_id: productID,
      csrfmiddlewaretoken: csrfmiddlewaretoken
    },
    success: function (response) {
      console.log("response");
      window.location.reload();
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log(errorThrown);
      // handle the error case
    }
  });
}
function applyCoupon(total_price, total_tax){
  $('#total-price').text(total_price)
  $('#total-tax').text(total_tax)

  formatPriceInToman(document.getElementById("total-price"))
  formatPriceInToman(document.getElementById("total-tax"))
}
function validateCoupon(){
  const code = $('#coupon-code').val()
  const url = $('#coupon-code').data('url')
  const csrfmiddlewaretoken = $('#coupon-code').data('csrf')
  console.log(code, url, csrfmiddlewaretoken)
  $.ajax({
    method: 'POST',
    url: url,
    data: {
      code: code,
      csrfmiddlewaretoken: csrfmiddlewaretoken,

    },
    success: function(response) {
      console.log(response)
      Toastify({
        text:response.message,
        className: `info`,
        style: {
          background: "linear-gradient(to right, #00b09b, #96c93d)",
          }
      }).showToast();
      applyCoupon(response.total_price, response.total_tax)
      // applyDiscount(response.total_price,response.total_tax)
    },
    error: function(jqXHR,textStatus, errorThrown) {
      Toastify({
        text:jqXHR.responseJSON.message,
        className: `error`,
        style: {
          background: "red",
        }
      }).showToast();
    }
  })
}


function addToWishlist(element, productId){
  // console.log(element.getAttribute('class'))
  // console.log(element.getAttribute('title'))
  // console.log(element.dataset.url)
  // console.log(element.dataset.csrf)


  const url = element.dataset.url
  const csrfmiddlewaretoken = element.dataset.csrf
  $.ajax({
    method: 'POST',
    url : url,
    data : {
      'product_id': productId,
      'csrfmiddlewaretoken': csrfmiddlewaretoken
    },
    success: function(response){
      Toastify({
        text:response.message,
        className: `info`,
        style: {
          background: "linear-gradient(to right, #00b09b, #96c93d)",
          }
      }).showToast();
      $(element).toggleClass('active');
    },
    error: function(jqXHR,textStatus, errorThrown) {
      Toastify({
        text:jqXHR.responseJSON.message,
        className: `error`,
        style: {
          background: "red",
        }
      }).showToast();
    }
  })
}