$(document).ready(function() {
    "use strict";
    // Animate loader off screen
    $(' .preloader').fadeOut("fast");


// ........................................................................HOME.........................................................................

//home page Silder
$('#silder_carousel').owlCarousel({
    // loop: true,  
    autoPlay: 3000,
    animateIn: 'fadeIn',
    animateOut: 'fadeOut',
    loop: false,
    navigationText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
    navigation: false,
    pagination: true,
    responsive: {
        0: {
            items: 1
        },
        380: {
            items: 1
        },
        576: {
            items: 1
        },
        992: {
            items: 1
        },
        1409: {
            items: 1
        },
        1850: {
            items: 1
        }
    }
})
	
});


//plus minus quantity
$('.btn-number').click(function(e) {
    e.preventDefault();

    fieldName = $(this).attr('data-field');
    type = $(this).attr('data-type');
    var input = $("input[name='" + fieldName + "']");
    var currentVal = parseInt(input.val());
    if (!isNaN(currentVal)) {
        if (type == 'minus') {

            if (currentVal > input.attr('min')) {
                input.val(currentVal - 1).change();
            }
            if (parseInt(input.val()) == input.attr('min')) {
                $(this).attr('disabled', true);
            }

        } else if (type == 'plus') {

            if (currentVal < input.attr('max')) {
                input.val(currentVal + 1).change();
            }
            if (parseInt(input.val()) == input.attr('max')) {
                $(this).attr('disabled', true);
            }

        }
    } else {
        input.val(0);
    }
});
$('.input-number').focusin(function() {
    $(this).data('oldValue', $(this).val());
});
$('.input-number').change(function() {

    minValue = parseInt($(this).attr('min'));
    maxValue = parseInt($(this).attr('max'));
    valueCurrent = parseInt($(this).val());

    name = $(this).attr('name');
    if (valueCurrent >= minValue) {
        $(".btn-number[data-type='minus'][data-field='" + name + "']").removeAttr('disabled')
    } else {
        alert('Sorry, the minimum value was reached');
        $(this).val($(this).data('oldValue'));
    }
    if (valueCurrent <= maxValue) {
        $(".btn-number[data-type='plus'][data-field='" + name + "']").removeAttr('disabled')
    } else {
        alert('Sorry, the maximum value was reached');
        $(this).val($(this).data('oldValue'));
    }

});
//plus minus quantity


// special product
$('#fullcarousel').owlCarousel({
    // loop: true,  
    pagination: false,
    navigation: false,
    nav: true,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        380: {
            items: 1
        },
        576: {
            items: 1
        },
        768: {
            items: 1
        },
        1200: {
            items: 2
        },
        1410: {
            items: 2
        },
        1850: {
            items: 2
        }

    }
})




// top product

$('#product_carousel2').owlCarousel({
    // loop: true,  
    pagination: false,
    navigation: false,
    nav: true,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 2
        },
        380: {
            items: 2
        },
        576: {
            items: 3
        },
        768: {
            items: 3
        },
        1200: {
            items: 5
        },
        1410: {
            items: 5
        },
        1850: {
            items: 6
        }
    }
})

// special_products

$('#special_products').owlCarousel({
    // loop: true,  
    pagination: false,
    navigation: false,
    nav: true,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        374: {
            items: 2
        },
        576: {
            items: 3
        },
        992: {
            items: 3
        },
        1199: {
            items: 4
        },
        1299: {
            items: 5
        },
        1589: {
            items: 6
        }
    }
})

// top product
$('.owl-carousel-1').owlCarousel({
    loop: false,
    pagination: false,
    navigation: false,
    nav: true,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: 3000,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        380: {
            items: 2
        },
        576: {
            items: 3
        },
        1199: {
            items: 3
        },
        1200: {
            items: 4
        },
        1299: {
            items: 5
        },
        1850: {
            items: 5
        }
    }
})


// blog 

$('#blog_carousel').owlCarousel({
    loop: true,
    pagination: false,
    navigation: false,
    dots: false,
    nav: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    slidesPerRow: 1,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: 3000,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        575: {
            items: 2
        },
        768: {
            items: 2
        },
        992: {
            items: 2
        },
        1199: {
            items: 2
        },
        1200: {
            items: 3
        },
        1410: {
            items: 3
        },
        1850: {
            items: 4,
        }
    }
})

// brand-logo


$('#logo_carousel').owlCarousel({
    // loop: true,  
    pagination: false,
    navigation: false,
    dots: false,
    nav: false,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 2
        },
        400: {
            items: 3
        },
        600: {
            items: 4
        },
        991: {
            items: 5
        },
        1200: {
            items: 5
        },
        1410: {
            items: 5
        },
        1850: {
            items: 8
        }
    }
})


//about us
$('#ab_customer').owlCarousel({
    // loop: true,  
    pagination: false,
    navigation: false,
    nav: false,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        992: {
            items: 2
        }
    }
})

var owl = $('.silder_carousel .owl-carousel');
owl.owlCarousel({
    items: 4,
    loop: true,
    margin: 10,
    autoplay: true,
    autoplayTimeout: 30000,
    autoplayHoverPause: true
});
$('.play').on('click', function() {
    owl.trigger('play.owl.autoplay', [1000])
})
$('.stop').on('click', function() {
    owl.trigger('stop.owl.autoplay')
})

/* menu more */
$(document).ready(function() {
    if (($(document).width() >= 1800)) {
        var count_block = $(' .h_menu  .level-1').length;
        var number_blocks = 11;
        if (count_block < number_blocks) {
            return false;
        } else {

            $('  .h_menu  .level-1').each(function(i, n) {
                if (i == number_blocks) {
                    $('  .h_menu ').append('<li class="view_more"><a><i class="fa fa-plus"></i><span>More</span></a></li>');
                }
                if (i > number_blocks) {
                    $(this).addClass('wr_hide_menu');
                }
            })
            $('.wr_hide_menu').hide();
            $('.view_more').click(function() {
                $(this).toggleClass('active');
                $('.wr_hide_menu').slideToggle();
            });
        }
    }
});

$(document).ready(function() {
    if (($(document).width() >= 1590) && ($(document).width() <= 1799)) {
        var count_block = $(' .h_menu  .level-1').length;
        var number_blocks = 11;
        if (count_block < number_blocks) {
            return false;
        } else {

            $('  .h_menu  .level-1').each(function(i, n) {
                if (i == number_blocks) {
                    $('  .h_menu ').append('<li class="view_more"><a><i class="fa fa-plus"></i><span>More</span></a></li>');
                }
                if (i > number_blocks) {
                    $(this).addClass('wr_hide_menu');
                }
            })
            $('.wr_hide_menu').hide();
            $('.view_more').click(function() {
                $(this).toggleClass('active');
                $('.wr_hide_menu').slideToggle();
            });
        }
    }
});

$(document).ready(function() {
    if (($(document).width() >= 1410) && ($(document).width() <= 1589)) {
        var count_block = $(' .h_menu  .level-1').length;
        var number_blocks = 9;
        if (count_block < number_blocks) {
            return false;
        } else {

            $('  .h_menu  .level-1').each(function(i, n) {
                if (i == number_blocks) {
                    $('  .h_menu ').append('<li class="view_more"><a><i class="fa fa-plus"></i><span>More</span></a></li>');
                }
                if (i > number_blocks) {
                    $(this).addClass('wr_hide_menu');
                }
            })
            $('.wr_hide_menu').hide();
            $('.view_more').click(function() {
                $(this).toggleClass('active');
                $('.wr_hide_menu').slideToggle();
            });
        }
    }
});

$(document).ready(function() {
    if (($(document).width() >= 1300) && ($(document).width() <= 1409)) {
        var count_block = $(' .h_menu  .level-1').length;
        var number_blocks = 8;
        if (count_block < number_blocks) {
            return false;
        } else {

            $('  .h_menu  .level-1').each(function(i, n) {
                if (i == number_blocks) {
                    $('  .h_menu ').append('<li class="view_more"><a><i class="fa fa-plus"></i><span>More</span></a></li>');
                }
                if (i > number_blocks) {
                    $(this).addClass('wr_hide_menu');
                }
            })
            $('.wr_hide_menu').hide();
            $('.view_more').click(function() {
                $(this).toggleClass('active');
                $('.wr_hide_menu').slideToggle();
            });
        }
    }
});

$(document).ready(function() {
    if (($(document).width() >= 1200) && ($(document).width() <= 1299)) {
        var count_block = $(' .h_menu  .level-1').length;
        var number_blocks = 8;
        if (count_block < number_blocks) {
            return false;
        } else {

            $('  .h_menu  .level-1').each(function(i, n) {
                if (i == number_blocks) {
                    $('  .h_menu ').append('<li class="view_more"><a><i class="fa fa-plus"></i><span>More</span></a></li>');
                }
                if (i > number_blocks) {
                    $(this).addClass('wr_hide_menu');
                }
            })
            $('.wr_hide_menu').hide();
            $('.view_more').click(function() {
                $(this).toggleClass('active');
                $('.wr_hide_menu').slideToggle();
            });
        }
    }
});

$(document).ready(function() {
    if (($(document).width() >= 992) && ($(document).width() <= 1199)) {
        var count_block = $('  .h_menu  .level-1').length;
        var number_blocks = 6;
        if (count_block < number_blocks) {
            return false;
        } else {

            $('  .h_menu  .level-1').each(function(i, n) {
                if (i == number_blocks) {
                    $('  .h_menu ').append('<li class="view_more"><a><i class="fa fa-plus"></i><span>More</span></a></li>');
                }
                if (i > number_blocks) {
                    $(this).addClass('wr_hide_menu');
                }
            })
            $('.wr_hide_menu').hide();
            $('.view_more').click(function() {
                $(this).toggleClass('active');
                $('.wr_hide_menu').slideToggle();
            });
        }
    }
});

/* menu more */

/* responsive menu */
function openNav() {
    $('body').addClass("active");
    document.getElementById("mySidenav").style.width = "280px";
}

function closeNav() {
    $('body').removeClass("active");
    document.getElementById("mySidenav").style.width = "0";
}
/* responsive menu */

// append-header

$(document).ready(function() {
    if ($(window).width() < 992) {
        // $( ".input-class" ).appendTo( ".header-top " );
        $(".top_menu").appendTo(".header-top ");
        $(".enter_pin").appendTo(".app_enter_pin");
        $(".navbar-header").appendTo(".head-logo");
        $(".md_acc").appendTo(".md_login ");
        $(".md_compare").appendTo(".md_login ");
        $(".md_wish").appendTo(".md_login ");
        $(".md_1").appendTo(".md_login ");
        $(".md_2").appendTo(".md_login ");
    }
    if ($(window).width() <= 767) {
        $(".main-menu .vertical_main_menu").appendTo(".main_sum_menu");
        $(".right_append").appendTo(".rightoleft_app");
    }
    if ($(window).width() <= 599) {
        $(".input-class").appendTo(".header-top");
    }
});
// append-header

$('.user span').click(function(event) {
    $(this).toggleClass('active');
    event.stopPropagation();
    $(".head_").slideToggle("fast");
    return false;
});

// ....................................................................../  HOME.........................................................................

// append-header

$(document).ready(function() {
    if ($(window).width() > 991) {
        $("#sp_vertical_menu .vertical_menu ").insertBefore("#sp_header_top .col-lg-9.text-left");
    }
});

//onclick image

function myFunction(imgs) {
    var expandImg = document.getElementById("expandedImg");
    expandImg.src = imgs.src;
    imgText.innerHTML = imgs.alt;
    expandImg.parentElement.style.display = "block";
}


// ...............................................................SINGLE PRODUCT PAGE....................................................................
// append-header

$(document).ready(function() {
    if ($(window).width() > 991) {
        $("#sp_vertical_menu .vertical_menu ").insertBefore("#sp_header_top .col-lg-9.text-left");
    }
});


//product carousel

$(document).ready(function() {
    $("#sp_pro_carousel").owlCarousel({
        itemsCustom: [
            [0, 2],
            [381, 3],
            [600, 4],
            [768, 3],
            [1410, 4]
        ],
        //autoPlay: 6000,
        loop: true,
        navigationText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
        navigation: true,
        pagination: false
    });
});


//onclick image

function myFunction(imgs) {
    var expandImg = document.getElementById("expandedImg");
    expandImg.src = imgs.src;
    imgText.innerHTML = imgs.alt;
    expandImg.parentElement.style.display = "block";
}


//related product

$('#related_product_carousel').owlCarousel({
    loop: true,  
    pagination: true,
    navigation: true,
    nav: true,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: 3000,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        374: {
            items: 2
        },
        576: {
            items: 3
        },
        992: {
            items: 3
        },
        1199: {
            items: 4
        },
        1299: {
            items: 5
        },
        1589: {
            items: 6
        }
    }
})


//custom product

$('#custom_product_carousel').owlCarousel({
    // loop: true,  
    pagination: false,
    navigation: true,
    nav: true,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: 3000,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        374: {
            items: 2
        },
        576: {
            items: 3
        },
        992: {
            items: 3
        },
        1199: {
            items: 4
        },
        1299: {
            items: 5
        },
        1589: {
            items: 6
        }
    }
})




// ............................................................./  SINGLE PRODUCT PAGE....................................................................

// .....................................................................  SHOP  ..........................................................................

$('#list-view').click(function() {
    $('.product-grid > .clearfix').remove();

    $('.product-grid').attr('class', 'item product-layout product-list col-xl-12 col-lg-12 col-md-12 col-sm-6 col-6');
    $('#grid-view').removeClass('active');
    $('#list-view').addClass('active');

    localStorage.setItem('display', 'list');
});

// Product Grid
$('#grid-view').click(function() {
    $('.product-list').attr('class', 'item product-layout product-grid col-xl-3 col-lg-4 col-md-4 col-sm-6 col-6');
    $('#list-view').removeClass('active');
    $('#grid-view').addClass('active');

    localStorage.setItem('display', 'grid');
});

if (localStorage.getItem('display') == 'list') {
    $('#list-view').trigger('click');
    $('#list-view').addClass('active');
} else {
    $('#grid-view').trigger('click');
    $('#grid-view').addClass('active');
}

// $(document).ready(function(){
//   var owl = $('#gallery_01');
//   owl.owlCarousel({
//     loop:true,
//     margin:10,
//     nav:false,
//     items: 5,
//   });

//   // Custom Button
//   $('.customNextBtn').click(function() {
//     owl.trigger('next.owl.carousel');
//   });
//   $('.customPreviousBtn').click(function() {
//     owl.trigger('prev.owl.carousel');
//   });

// });
$(document).on('click', '.sort_by', function() {
    $(this).addClass('active').siblings().removeClass('active')
})

// ..................................................................../  SHOP  ...........................................................................

//scroll
$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('#scroll').fadeIn();
        } else {
            $('#scroll').fadeOut();
        }
    });
    $('#scroll').click(function() {
        $("html, body").animate({
            scrollTop: 0
        }, 600);
        return false;
    });
});
//scroll

$('.gallery').each(function() {
    $(this).magnificPopup({
        delegate: 'a',
        type: 'image',
        gallery: {
            enabled: true
        }
    });
});

$(document).ready(function() {
    $(".filter-tag").click(function() {
        $(this).remove();
    });
});

//category style (category style page)

$('#cat_style3_carousel').owlCarousel({
    loop: true,
    pagination: false,
    navigation: false,
    dots: false,
    nav: false,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 2
        },
        400: {
            items: 3
        },
        600: {
            items: 4
        },
        991: {
            items: 5
        },
        1200: {
            items: 5
        },
        1410: {
            items: 5
        },
        1850: {
            items: 8
        }
    }
})

$('#cat_style1_carousel').owlCarousel({
    loop: true,
    pagination: false,
    navigation: false,
    dots: false,
    nav: false,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 2
        },
        400: {
            items: 3
        },
        600: {
            items: 4
        },
        991: {
            items: 5
        },
        1200: {
            items: 5
        },
        1410: {
            items: 5
        },
        1850: {
            items: 8
        }
    }
})

// multi product

$('#multi_product_1').owlCarousel({
    loop: true,
    pagination: false,
    navigation: false,
    dots: false,
    nav: false,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        400: {
            items: 3
        },
        600: {
            items: 4
        },
        991: {
            items: 5
        },
        1200: {
            items: 2
        },
        1410: {
            items: 3
        },
        1850: {
            items: 2
        }
    }
})

$('#multi_product_2').owlCarousel({
    loop: true,
    pagination: false,
    navigation: false,
    dots: false,
    nav: false,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        400: {
            items: 3
        },
        600: {
            items: 4
        },
        991: {
            items: 5
        },
        1200: {
            items: 2
        },
        1410: {
            items: 3
        },
        1850: {
            items: 2
        }
    }
})

$('#multi_product_3').owlCarousel({
    loop: true,
    pagination: false,
    navigation: false,
    dots: false,
    nav: false,
    navText: [
        "<i class='fa fa-chevron-left'></i>",
        "<i class='fa fa-chevron-right'></i>"
    ],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        400: {
            items: 3
        },
        600: {
            items: 4
        },
        991: {
            items: 5
        },
        1200: {
            items: 2
        },
        1410: {
            items: 3
        },
        1850: {
            items: 2
        }
    }
})


/* myFunction toggles between adding and removing the show class, which is used to hide and show the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {

    if (!event.target.matches('.dropbtn')) {

        var dropdowns = document.getElementsByClassName("dropdown-content");

        for (let i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}