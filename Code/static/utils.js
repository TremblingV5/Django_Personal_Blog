funciton showFrameLayer(target, title){
    layer.open({
      type: 2,
      title: title,
      shadeClose: true,
      shade: false,
      maxmin: true,
      area: ['893px', '600px'],
      content: target
    });
}