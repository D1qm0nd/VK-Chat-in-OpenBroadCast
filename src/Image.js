import './Image.css'
import MessageBox from './MessageBox'
import Message from './Message'

function Image({ img, userAvtr, UsrNick}) {
    return (
        <MessageBox>
            <Message img={userAvtr} userName={ UsrNick } message=""/>
            <img className='ImageMessage' src={img}></img>
        </MessageBox>
        );
}

export default Image;