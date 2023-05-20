import '../styles/style.css';
export default function RootLayout({ children }) {
    return (
      <html lang="en">
        <body className='bg-gradient-to-r from-slate-900 to-slate-700 h-screen text-slate-50'>{children}</body>
      </html>
    );
  }