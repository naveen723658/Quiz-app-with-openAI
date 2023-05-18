export default function Background() {
  return (
    <>
      <div
        style={{ top: "0.5rem", right: "42%" }}
        className="absolute rounded-full drop-shadow-2xl w-56 h-56 bg-gradient-to-r from-cyan-400 via-blue-500 to-sky-600 shadow-2xl"
      />
      <div
        style={{ bottom: "0.5rem", right: "7rem" }}
        className="absolute rounded-full drop-shadow-2xl w-56 h-56 bg-gradient-to-r from-cyan-400 via-blue-500 to-sky-600 shadow-2xl"
      />
    </>
  );
}
