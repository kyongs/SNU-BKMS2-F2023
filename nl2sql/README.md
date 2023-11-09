# Assignment 3.
[link](./assignment3.md)

# Practice 4. EverSQL vs. ChatGPT

For Practice 4, you will use EverSQL and ChatGPT for NL2SQL, and compare the results between them.<br/>

Write the natural language queries below in the prompt of ChatGPT and EverSQL.
Then, compare the queries genereted from each tool, and the answer.

- **Database**: Oracle 19c
- **Schema**: https://www.db-book.com/university-lab-dir/sample_tables-dir/index.html -> DDL script
- **Tools**: [EverSQL](https://www.eversql.com/text-to-sql/), [ChatGPT](https://chat.openai.com/)


## Natural Language Query
1. Find all instructors earning the highest salary. There may be more than one with the same salary. <br/>
2. Display a list of all instructors, show each instructor’s ID and the number of sections taught. Make sure to show the number of sections as 0 for instructors who have not taught any section. Your query should use an outer join, and should not use subqueries.<br/>
3. Find all courses taught in both the Fall 2017 semester and in the Spring 2018 semester. <br/>
4. Find every pair such that pre is directly or indirectly a prerequisite for course cid. <br/>
5. Find all courses that were offered at most once in 2017.<br/>


## EverSQL vs. ChatGPT
-   Ex) 1. Find all instructors earning the highest salary. There may be more than one with the same salary.
    ```sql
    ##EVERSQL
    SELECT
    *
    FROM
    instructor
    WHERE
    salary = (
        SELECT
        MAX(salary)
        FROM
        instructor
    )
    ```

    ```sql
    ##CHATGPT WITHOUT SCHEMA INFORMATION
    SELECT *
    FROM Instructors
    WHERE Salary = (SELECT MAX(Salary) FROM Instructors);
    ```

    ```sql
    ##CHATGPT WITH SCHEMA INFORMATION
    SELECT ID, name, dept_name, salary
    FROM instructor
    WHERE salary = (SELECT MAX(salary) FROM instructor);
    ```
    ```sql
    # TEXTBOOK ANSWER
    SELECT ID, name FROM instructor
    WHERE salary = (SELECT MAX(salary) FROM instructor);
    ```



## Answer (From Textbook "Database System Concepts")
1. Find all instructors earning the highest salary. There may be more than one with the same salary.
   ```sql
    SELECT ID, name FROM instructor
    WHERE salary = (SELECT MAX(salary) FROM instructor);
    ```
2. Display a list of all instructors, show each instructor’s ID and the number of sections taught. Make sure to show the number of sections as 0 for instructors who have not taught any section. Your query should use an outer join, and should not use subqueries.
   ```sql
   SELECT ID, COUNT(sec_id) AS Number_of_sections
   FROM instructor
   NATURAL LEFT OUTER JOIN
   teaches
   GROUP BY ID;
   ```
3. Find all courses taught in both the Fall 2017 semester and in the Spring 2018 semester.
   ```sql
   SELECT course_id, title
   FROM section AS S
   WHERE semester = 'Fall'
   AND TEAR=2017
   AND EXISTS ( 
    SELECT * FROM section AS T
    WHERE semester = 'Spring'
    AND year = 2018
    AND S.course_id = T.course_id
   );
   ```
4. Find every pair such that pre is directly or indirectly a prerequisite for course cid.
   ```sql
   WITH RECURSIVE rec_prereq(course_id, prereq_id) 
   AS (
    SELECT course_id, prereq_id
    FROM prereq
    UNION
    SELECT rec_prereq.course_id, prereq.prereq_id
    FROM rec_prereq, prereq
    WHERE rec_prereq.prereq_id = prereq.course_id
   )
   SELECT * FROM rec_prereq;
   ```
5. Find all courses that were offered at most once in 2017.
   ```sql
   SELECT T.course_id,
   FROM course AS T
   WHERE UNIQUE (
    SELECT R.course_id
    FROM section AS R
    WHERE T.course_id = R.course_id
    AND R.year = 2017
   );
   ```
