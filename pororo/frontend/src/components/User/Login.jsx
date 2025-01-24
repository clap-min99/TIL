import { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // React Router의 useNavigate 훅
import api from './api'; // Axios 인스턴스 불러오기
import './index.css';
import logo from '../../assets/logo.png'; // 로고 이미지 경로 확인 필요

const Login = () => {
  const [formData, setFormData] = useState({
    user_id: '', // 아이디
    password: '', // 비밀번호
  });

  const navigate = useNavigate(); // 페이지 이동을 위한 훅

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.user_id || !formData.password) {
      alert('아이디와 비밀번호를 입력해주세요.');
      return;
    }

    api
      .post('/auth/login', formData)
      .then((response) => {
        // 성공 시
        const { token, refreshToken } = response.data; // 서버로부터 Access 토큰과 Refresh 토큰 받기
        localStorage.setItem('token', token); // Access 토큰 저장
        localStorage.setItem('refreshToken', refreshToken); // Refresh 토큰 저장
        alert('로그인 완료!');
        navigate('/main'); // 로그인 성공 후 메인 페이지로 이동
      })
      .catch((error) => {
        // 실패 시
        console.error('Error during login:', error);
        if (error.response) {
          alert(error.response.data.message || '로그인에 실패했습니다.');
        } else {
          alert('서버와 연결할 수 없습니다.');
        }
      });
  };

  return (
    <div className="form-container">
      <img src={logo} alt="마래바 로고" className="logo" />
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <input
            className="input"
            type="text"
            id="user_id"
            name="user_id"
            placeholder="아이디"
            value={formData.user_id}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <input
            className="input"
            type="password"
            id="password"
            name="password"
            placeholder="비밀번호"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <button className="button" type="submit">
          로그인
        </button>
      </form>
      <div className="secondary-button">
        <span onClick={() => navigate('/find-id')}>아이디 찾기</span> |{' '}
        <span onClick={() => navigate('/find-pw')}>비밀번호 찾기</span>
      </div>
      <div>
        <button className="secondary-button" onClick={() => navigate('/signup')}>
          회원가입하기
        </button>
      </div>
       {/* /main으로 이동하는 임시 버튼 */}
       <div>
        <button className="secondary-button" onClick={() => navigate('/main')}>
          메인 페이지로 이동
        </button>
      </div>
    </div>
  );
};

export default Login;
