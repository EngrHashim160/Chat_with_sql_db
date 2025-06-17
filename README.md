# Chat with SQL Database

A Streamlit application that enables natural language conversations with SQL databases using LangChain and Groq's language models. This tool allows users to query databases using plain English and get intelligent responses.

## 🚀 Features

- **Natural Language to SQL**: Ask questions in plain English and get SQL query results
- **Multiple Database Support**: Works with SQLite and MySQL databases
- **Interactive Chat Interface**: Streamlit-based chat UI with message history
- **Real-time Streaming**: Live response streaming using Groq's fast inference
- **Database Flexibility**: Switch between local SQLite and remote MySQL databases
- **Intelligent SQL Agent**: Uses LangChain's SQL agent with zero-shot reasoning

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/LLM**: LangChain + Groq (Llama3-8b-8192)
- **Database**: SQLite (local) / MySQL (remote)
- **SQL Integration**: SQLAlchemy + LangChain SQL Database Toolkit

## 📋 Prerequisites

- Python 3.8+
- Groq API key
- MySQL database (optional, for remote database connection)

## 🔧 Installation

1. **Navigate to the project directory**
   ```bash
   cd Chat_with_sql_db
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit langchain langchain-groq sqlalchemy mysql-connector-python
   ```

3. **Set up the sample database (optional)**
   ```bash
   python sqlite.py
   ```
   This creates a `student.db` file with sample student data.

## 🚀 Usage

### Starting the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

### Configuration Options

#### Option 1: SQLite Database (Default)
- Select "Use SQLLite 3 Database- Student.db" in the sidebar
- Uses the local `student.db` file with sample student data
- No additional configuration required

#### Option 2: MySQL Database
- Select "Connect to you MySQL Database" in the sidebar
- Provide the following connection details:
  - MySQL Host (e.g., `localhost` or `your-server.com`)
  - MySQL User (e.g., `root`)
  - MySQL Password
  - MySQL Database name

### API Key Setup
- Enter your Groq API key in the sidebar
- Get your free API key from [Groq Console](https://console.groq.com/)

## 💬 Example Queries

Once the application is running, you can ask questions like:

### For Student Database:
- "How many students are there in total?"
- "Show me all students in Data Science class"
- "What is the average marks of students?"
- "Who scored the highest marks?"
- "List students in section A"
- "How many students are in each class?"

### General SQL Queries:
- "What tables are available in this database?"
- "Describe the structure of the STUDENT table"
- "Show me the top 3 students by marks"
- "Count students by section"

## 📊 Sample Database Schema

The included `student.db` contains a STUDENT table with the following structure:

| Column  | Type        | Description           |
|---------|-------------|-----------------------|
| NAME    | VARCHAR(25) | Student name          |
| CLASS   | VARCHAR(25) | Course/Class name     |
| SECTION | VARCHAR(25) | Section identifier    |
| MARKS   | INT         | Student marks/score   |

### Sample Data:
- Hashim - Data Science, Section A, 90 marks
- Izaz - Data Science, Section B, 80 marks
- Abubakar - Devops, Section A-, 85 marks
- Sohail - Network Communication, Section A, 90 marks
- Adil - Web Development, Section A, 90 marks

## 🔧 Configuration

### Environment Variables (Optional)
You can set environment variables instead of entering credentials in the UI:

```bash
export GROQ_API_KEY=your_groq_api_key
export MYSQL_HOST=your_mysql_host
export MYSQL_USER=your_mysql_user
export MYSQL_PASSWORD=your_mysql_password
export MYSQL_DATABASE=your_database_name
```

### Database Connection Strings
The application supports various database connection formats:

- **SQLite**: `sqlite:///path/to/database.db`
- **MySQL**: `mysql+mysqlconnector://user:password@host/database`

## 🎯 How It Works

1. **User Input**: User types a natural language question
2. **LLM Processing**: Groq's Llama3 model interprets the question
3. **SQL Generation**: LangChain's SQL agent generates appropriate SQL queries
4. **Database Execution**: Query is executed against the selected database
5. **Response Generation**: Results are formatted into a natural language response
6. **Streaming Output**: Response is streamed back to the user in real-time

## 🔒 Security Features

- **Read-only Access**: SQLite database is opened in read-only mode
- **SQL Injection Protection**: LangChain's SQL agent includes built-in protections
- **Credential Masking**: Database passwords are masked in the UI
- **Session Management**: API keys are stored only in session state

## 🐛 Troubleshooting

### Common Issues

1. **"Please add the groq api key"**
   - Ensure you've entered a valid Groq API key in the sidebar

2. **"Please provide all MySQL connection details"**
   - Fill in all required MySQL connection fields
   - Verify your database credentials are correct

3. **Database connection errors**
   - Check if MySQL server is running (for MySQL option)
   - Verify database credentials and network connectivity
   - Ensure the database exists and is accessible

4. **"No such table" errors**
   - Run `python sqlite.py` to create the sample database
   - Verify the database file exists in the project directory

### Performance Tips
- Use specific questions for better results
- The SQLite option is faster for testing and demos
- MySQL option is better for production databases

## 📝 File Structure

```
Chat_with_sql_db/
├── app.py          # Main Streamlit application
├── sqlite.py       # Database setup script
├── student.db      # Sample SQLite database
└── README.md       # This file
```

## 🔮 Future Enhancements

- Support for PostgreSQL and other databases
- Query history and favorites
- Data visualization capabilities
- Export query results to CSV/Excel
- Advanced SQL query optimization suggestions
- Multi-table relationship understanding
- Custom database schema upload

## 📞 Support

For issues and questions:
- Check the troubleshooting section above
- Verify your API key and database connections
- Ensure all dependencies are properly installed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with both SQLite and MySQL
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Note**: This tool is designed for querying and analyzing data. Always ensure you have proper permissions before connecting to production databases.
