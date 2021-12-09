$(document).ready(function (){

    $('form.ajax').on('submit', function(e){
        e.preventDefault();

        var $this = $(this)
        var url = $this.attr("action")
        var method = $this.attr("method")

        $.ajax({
            type : method,
            url : url,
            dataType:"json",
            data : new FormData(this),
            processData : false,
            contentType : false,
            cache : false,

            success:function(data){
                var title = data["title"]
                var text = data["message"]
                var status = data["status"]

                Swal.fire({
                    icon: status,
                    title: title,
                    text : text
                })
                if(status == "success"){
                    $this.trigger("reset")
                }
            },
            error: function(data){
                console.log("An Error Ocuured");
            },
        })
    })
})