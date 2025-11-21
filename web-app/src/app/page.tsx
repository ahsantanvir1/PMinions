export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      {/* Hero Section */}
      <main className="container mx-auto px-4 py-16">
        <div className="flex flex-col items-center text-center space-y-8">
          {/* Logo/Title */}
          <div className="space-y-4">
            <h1 className="text-6xl font-bold bg-gradient-to-r from-blue-600 to-violet-600 bg-clip-text text-transparent">
              🤖 PMinions
            </h1>
            <p className="text-2xl text-gray-600 max-w-2xl">
              AI-Powered Desktop Agents for Project Management Automation
            </p>
          </div>

          {/* Value Proposition */}
          <div className="max-w-3xl space-y-4">
            <p className="text-xl text-gray-700">
              Empower project managers to focus on strategic decisions by automating 
              repetitive administrative tasks through intelligent, locally-running AI agents.
            </p>
          </div>

          {/* CTA Buttons */}
          <div className="flex gap-4 pt-8">
            <button className="px-8 py-4 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl">
              Get Started
            </button>
            <button className="px-8 py-4 bg-white text-blue-600 border-2 border-blue-600 rounded-lg font-semibold hover:bg-blue-50 transition-colors">
              Watch Demo
            </button>
          </div>

          {/* Status Badge */}
          <div className="pt-8">
            <span className="inline-flex items-center px-4 py-2 rounded-full bg-yellow-100 text-yellow-800 text-sm font-medium">
              🚧 In Development - Coming Soon
            </span>
          </div>

          {/* Features Preview */}
          <div className="grid md:grid-cols-3 gap-8 pt-16 w-full max-w-5xl">
            <div className="p-6 bg-white rounded-lg shadow-md">
              <div className="text-4xl mb-4">⚡</div>
              <h3 className="text-xl font-semibold mb-2">Fast Setup</h3>
              <p className="text-gray-600">
                From signup to first automation in under 10 minutes
              </p>
            </div>
            
            <div className="p-6 bg-white rounded-lg shadow-md">
              <div className="text-4xl mb-4">🔒</div>
              <h3 className="text-xl font-semibold mb-2">Privacy First</h3>
              <p className="text-gray-600">
                Agents run locally - your data stays on your machine
              </p>
            </div>
            
            <div className="p-6 bg-white rounded-lg shadow-md">
              <div className="text-4xl mb-4">🧠</div>
              <h3 className="text-xl font-semibold mb-2">AI-Powered</h3>
              <p className="text-gray-600">
                Smart automation using GPT-4 for complex decisions
              </p>
            </div>
          </div>

          {/* Coming Soon Features */}
          <div className="pt-16 w-full max-w-5xl">
            <h2 className="text-3xl font-bold mb-8">First Agent: Project Booking & Initiation</h2>
            <div className="bg-white p-8 rounded-lg shadow-md text-left">
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <span>Automatically parse project assignment emails</span>
                </li>
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <span>Extract project codes (AEMA-xxxxx format)</span>
                </li>
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <span>Create and organize network folders automatically</span>
                </li>
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <span>AI-powered email recognition and validation</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="container mx-auto px-4 py-8 mt-16 border-t">
        <div className="text-center text-gray-600">
          <p>© 2025 PMinions. All rights reserved.</p>
          <p className="text-sm mt-2">Status: 🟡 In Development | Version: 0.1.0</p>
        </div>
      </footer>
    </div>
  );
}
