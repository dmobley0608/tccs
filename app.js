const path = require('path');
const express = require("express");
const ejsMate = require("ejs-mate")
const nodemailer = require("nodemailer")


const app = express();
app.use(express.urlencoded({ extended: true }))

// Template Config
app.engine('ejs', ejsMate)
app.set('view engine', 'ejs')
app.set('views', path.join(__dirname, "views"))
app.use("/static", express.static(path.join(__dirname, "public")))

app.get('/', (req,res)=>{
    res.render('index')
})

app.post('/', (req, res)=>{
    const {name, email, message} = req.body;
    const mail = {
        from: "support@tccs.tech",
        to:"dmobley0608@gmail.com",
        subject:"New Request",
        text:`From:${name}, \n${email}: \n\n${message}`
    }
    const reply = {
        from: "support@tccs.tech",
        to:email,
        subject:"Thank You For Reaching Out",
        text: "Thank you for reaching out to TCCS.TECH. We will be in touch with you shortly!"
    }
    try{
        const transporter = nodemailer.createTransport({
            service:'gmail',
            auth:{
                user:'dmobley0608@gmail.com',
                pass:'iothagfoexqjiqxc'
            }
        });
        transporter.sendMail(mail)
        transporter.sendMail(reply)
    }catch(e){
        console.log(e)
    }

    res.redirect('/')
   
})

app.listen(3000, ()=>{
    console.log('running on port 3000') 
}) 