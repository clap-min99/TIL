import { useNavigate } from 'react-router-dom';
import './index.css';

const StageTwo = () => {
  const navigate = useNavigate(); // 페이지 이동을 위한 React Router 훅

  return (
    <div className="stage-two-container">
      <button className="home-button" onClick={() => navigate('/single')}>
      ↩
      </button>
      <h1>단어와 친해지기</h1>
      <p>호끌락칩스 투게더 버번위스키</p>
    </div>
  );
};

export default StageTwo;
