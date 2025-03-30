import { Slot } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';

// This _layout.tsx file acts as the "App.js" in a traditional React Native project.
// It's the root layout for all screens in the `app/` folder.
// Any screen (like /dashboard or /goals) will be rendered inside the <Slot />.

// You can wrap global providers here (ThemeProvider, AuthContext, etc.)
// You can also define UI elements that should be persistent across pages.

export default function Layout() {
  return (
    <SafeAreaView style={{ flex: 1 }}>
      {/* Sets the status bar style for all screens */}
      <StatusBar style="dark" />

      {/* Renders the current route's screen */}
      <Slot />

      {/* Add a global footer/nav bar here if needed */}
    </SafeAreaView>
  );
}
