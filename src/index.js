import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Message from './Message';
import Image from './Image'
import reportWebVitals from './reportWebVitals';
import data from './logs.json';

/*const messages = [{ id: '1', avatar: 'https://i.imgur.com/2ylJq3q.jpg', name: 'Listik', text: 'Hello, world!'},
                  { id: '2', avatar: 'https://i.imgur.com/2ylJq3q.jpg', name: 'Listik', text: 'It`s me' },
                  { id: '3', avatar: 'https://i.imgur.com/2ylJq3q.jpg', name: 'Listik', text: 'El Psy Congro' },
                  { id: '4', avatar: 'https://i.imgur.com/2ylJq3q.jpg', name: 'Listik', text: 'loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text' }

];*/

const messageList = data.map(message =>
    <Message img={message.user.avatar} userName={message.user.name} message={message.message.text} />
);
console.log(messageList)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        { messageList }
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
