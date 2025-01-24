import { useNavigate } from 'react-router-dom';
import './index.css';

const StageOne = () => {
  const navigate = useNavigate(); // 페이지 이동을 위한 React Router 훅

  return (
    <div className="stage-one-container">
      <button className="home-button" onClick={() => navigate('/single')}>
        ↩
      </button>
      <h1 className="stage-one-title">발음 익히기</h1>

      <div className="card-slider">
        <div className="card">
          <h2>단모음</h2>
          <p>ㅏ, ㅓ, ㅗ, ㅜ, ㅡ, ㅣ</p>
          <button className="start-button">시작하기</button>
        </div>
        <div className="card">
          <h2>이중모음 1</h2>
          <p>ㅑ, ㅕ, ㅛ, ㅠ, ㅐ, ㅔ</p>
          <button className="start-button">시작하기</button>
        </div>
        <div className="card">
          <h2>이중모음 2</h2>
          <p>ㅒ, ㅖ, ㅘ, ㅙ, ㅚ</p>
          <button className="start-button">시작하기</button>
        </div>
        <div className="card">
          <h2>이중모음 3</h2>
          <p>ㅝ, ㅞ, ㅟ, ㅢ</p>
          <button className="start-button">시작하기</button>
        </div>
      </div>
    </div>
  );
};

export default StageOne;
