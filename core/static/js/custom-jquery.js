$(document).ready(function () {
  let urlParam = new URLSearchParams(window.location.search);
  $("#order-by-filter").val(urlParam.get("order_by"));
  $("#page-size-filter").val(urlParam.get("page_size"));
  $("#search-query-filter").val(urlParam.get("q"));
  $("#min-price-filter").val(urlParam.get("min_price"));
  $("#max-price-filter").val(urlParam.get("max_price"));
  urlParam.getAll("categories").forEach((element) => {
    if (element === $(`#categories-filter-${element}`).val()) {
      $(`#categories-filter-${element}`).prop("checked", true);
    }
  });

  $("#order-by-filter").change(function () {
    selectionOption = $(this).val();
    urlParam.set("order_by", selectionOption);
    let newUrl = window.location.pathname + "?" + urlParam.toString();
    window.location.href = newUrl;
  });

  $("#page-size-filter").change(function () {
    selectionOptionPage = $(this).val();
    urlParam.set("page_size", selectionOptionPage);
    let newUrlPage = window.location.pathname + "?" + urlParam.toString();
    window.location.href = newUrlPage;
  });

});