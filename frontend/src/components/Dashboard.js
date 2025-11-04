import React, { useEffect, useState } from "react";
import axios from "axios";

const Dashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("/api/students").then((res) => setData(res.data));
  }, []);

  return (
    <div>
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Student ID</th>
            <th>Course ID</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, idx) => (
            <tr key={idx}>
              <td>{row.student_id}</td>
              <td>{row.course_id}</td>
              <td>{row.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Dashboard;
