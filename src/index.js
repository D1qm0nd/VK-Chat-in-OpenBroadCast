import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Message from './components/Message';
import MessageArea from './components/MessageArea';
import reportWebVitals from './reportWebVitals';
import data from './viewlogs.json';



/*class Chat extends React.Component {
    constructor(props) {
        super(props);
        let count = 0;
        this.messageList = data.map(message =>
            <Message key={count++} msg_id={count} img={message.user.avatar} userName={message.user.name} message={message.message.text} />
        );
    }

    render() {
        return (
            <MessageArea>
                this.messageList
            </MessageArea>
        );
    }
}*/

let count = 0;
var messageList = data.map(message =>
    <Message key={count++} msg_id={count} img={message.user.avatar} userName={message.user.name} message={message.message.text} />
);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <MessageArea>{messageList}</MessageArea>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
