# Assignment 3. How to Train ChatGPT for NL2SQL
This week, we will test how much more accurately ChatGPT can generate answers when additional information is provided through a simple schema. <br/>
Change *5 natural language queries* to *SQL queries* using ChatGPT.<br/>

You should prompt ChatGPT in three steps and analyze the result in the report. Three steps are as follows:

    1.  Ask ChatGPT to generate a SQL query **without giving any schema information**.
    2.  Ask ChatGPT to generate a SQL query **with schema information**.
    3. Give **some additional information**(i.e., explanation of table schema, PK/FK relationship, clause you want to use etc.) to ChatGPT to make the SQL query more accurate.

To verify if the SQL query generated by ChatGPT is correct, use LiveSQL. 


## Environments
- [ChatGPT](https://chat.openai.com/)
- [LiveSQL](https://livesql.oracle.com/)

## Natural Language Queries
1. Find the department that have the highest average salary.
2. Find the average total credits over all prior years.
3. List the last 25% of employees when ranking by salary.
4. Compute a year-over-year amount difference in sales table.
5. Show [1] the order date, [2] the number of orders for that date, [3] the number of books ordered, [4] the total price of the orders, [5] the running total of books for the month, [6] the number of books from the same day last week, and [7] all of these totals (from [1] to [6]) should also show for each month and overall.


## Table Information
- For problem 1 and 2, use this  [DDL file](./DDL(q1,q2).sql).
- For problem 3 and 4, use this [DDL file]().
- For problem 5, use this [DDL file]().

## Note
- Problem 1~4 is worth 15 points. Problem 5 is worth 20 points.*(not fixed, but in a high probability!)* The remaining 20 points will be allocated for the "conclusion and analysis".
- Queries generated by ChatGPT may not actually work in some cases, so you need to be validate on LiveSQL. (The query you last wrote in report will be used for grading.)
- **Please document the entire series of steps(all three steps) in the report until you get the final query as you refine the query through prompts.**
- If a query created by ChatGPT doesn't work, prompt it to provide a proper query by entering additional
information in the prompt, and document this process in a report. 
- You can choose columns as you wish for the SELECT statement.<br/>

## Submission Guide
> Due Date: 2023.11.15 11:59 PM
<br/>
> Where: ETL

1. Name of file should be **“Assignment3-studentID.pdf”**. (-10 points if the file format is not pdf)
2. Late submissions are penalized by **20%** of total grade per day. <br/>
3. Write the **ChatGPT version** you used in the report. <br/>
4. Download the [REPORT TEMPLATE](./report-template.docx). *(This is just a formatting example, write report in a free format.)*