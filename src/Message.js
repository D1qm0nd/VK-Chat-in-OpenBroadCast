import './Message.css';
import MessageBox from './MessageBox.js'

function Message({ msg_id, img, userName, message }) {
    return (
      <MessageBox>
          <div className="Message" id={msg_id}>
              <div className="UserAvtr">
                  <img className="Photo" src={img}></img>
                </div>
                <div className="Texts">
                    <h1 className="UserNick">{userName}</h1>
                    <h2 className="MessageText">{message}</h2>
                </div>
          </div>
      </MessageBox>
  );
}

export default Message;
