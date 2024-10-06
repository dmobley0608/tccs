console.log("%cHello fellow developers! I'm a software engineer with over 10 years experience. I'm always ready for a new challenge. If you're looking to collaborate on a project, send me a message. You'll find my contact information on this page. Looking forward to hearing from you.",'background: #222; color: #bada55; padding:15px;border-radius:10px;')

$('#loader').hide()
$('a').on('click',({currentTarget})=>{
  
    if(currentTarget.href.includes('#') && !window.location.href.includes('#')){
        $('#loader').show()
    }
})
$('button').on('click',()=>{
        $('#loader').show()    
})

$('form').on('submit',()=>{
    $('#loader').show()
})
