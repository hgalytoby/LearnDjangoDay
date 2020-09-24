$(function () {
    initTooSwiper();

    initSwiperMenu();
})


function initTooSwiper() {

    var swiper = new Swiper("#topSwiper", {
        loop: true,
        autoplay: 2000,
        pagination: '.swiper-pagination'
    });

}

function initSwiperMenu() {
    var swiper = new Swiper("#swiperMenu", {
        slidesPerView: 4
    });
}