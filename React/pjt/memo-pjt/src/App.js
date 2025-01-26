import './App.css';
import MemoContainer from './components/MemoContainer';
import SideBar from './components/SideBar';
import { useState } from 'react'

function App() {
  const [memos, setMemos] = useState([
    {
      title: 'Memo 1',
      content: 'This is memo 1',
      createdAt: 0, // 시간 값
      udpatedAt: 0, // 시간 값값
    },
    {
      title: 'Memo 2',
      content: 'This is memo 2',
      createdAt: 0, // 시간 값
      udpatedAt: 0, // 시간 값값
    }
  ])

  const [selectedMemoIndex, setSelectedMemoIndex] = useState(0)

  return (
    <div className="App">
      <SideBar memos={memos} />
      <MemoContainer memo={memos[selectedMemoIndex]}/>
    </div>
  );
}

export default App;
