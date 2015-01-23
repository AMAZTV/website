function create_modal(title, description) {
    console.log(description);
    document.getElementById('modal').innerHTML =
    ['<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">',
        '<div class="modal-dialog"><div class="modal-content">',
        '<div class="modal-header"><button type="button" class="close" data-dismiss="modal">',
        '<span aria-hidden="true">&times;</span><span class="sr-only">Close</span>',
        '</button>',
        '<h4 class="modal-title" id="myModalLabel">' + title + '</h4></div>',
        '<div class="modal-body">...</div>',
        '<div class="modal-footer"></div>',
        '</div></div></div>'
   ].join('\n');
}