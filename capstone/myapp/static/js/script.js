$(function(){

  // LIST-ITEM EVENT HANDLERS
  
  $('.list-group-item').on('mouseenter', function(e){
    $(this).addClass('mouseover');
  }).on('mouseleave', function(e){
    $(this).removeClass('mouseover');
  });
  
  $('.list-group-item').on('click', function(){
    console.log('clicked item');
  });

  // LIST-ITEM REMOVE BUTTON EVENT HANDLERS

  $('.remove-item').on('mouseenter', function(e){
    $(this).addClass('mouseover');
    $(this).parent().mouseleave();
  }).on('mouseleave', function(e){
    $(this).removeClass('mouseover');
    $(this).parent().mouseenter();
  });
  
  $('.remove-item').on('click', function(e){
    console.log('clicked remove-item btn');
    e.stopPropagation();
  });
  
});