import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';
import './App.css';

function App() {

    // new line start
    const [questionData, setQuestionData] = useState(null)

    function getData() {
        axios({
                method: "GET",
                url: "/questions",
            })
            .then((response) => {
                const res = response.data
                setQuestionData(({
                    name: res.name,
                    link: res.link
                }))
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }
    //end of new line 

    return ( <
        div className = "App" >
        <
        div className = "App-header" >
        <
        h1 className = "App-title" > CS Prep Kit < /h1> <
        p className = "App-desc" > Start your preparation via a Single Click < /p> <
        button className = "App-btn"
        onClick = { getData } > Generate Question < /button> <
        /div> <
        div className = 'App-content' > {
            questionData && < div >
            <
            div className = 'ques-container' >
            <
            p className = 'ques-content' > { questionData.name } < /p> <
            /div> <
            div className = 'ques-btn' >
            <
            a className = 'App-btn'
            href = { questionData.link }
            target = "_blank" > View Answer < /a> <
            /div> <
            /div>
        } <
        /div> <
        /div>
    );
}

export default App;