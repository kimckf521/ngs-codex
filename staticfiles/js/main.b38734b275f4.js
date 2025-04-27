// Navigation functionality
const navbar = document.querySelector(".navbar");
const navLinks = document.querySelector(".nav-links");
const menuToggle = document.querySelector(".menu-toggle");
const overlay = document.createElement("div");
overlay.className = "overlay";
document.body.appendChild(overlay);

// Toggle mobile menu
function toggleMenu() {
  navLinks.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("menu-open");
}

// Close menu when clicking outside or on a link
function closeMenu() {
  navLinks.classList.remove("active");
  overlay.classList.remove("active");
  document.body.classList.remove("menu-open");
}

// Event listeners
menuToggle.addEventListener("click", toggleMenu);
overlay.addEventListener("click", closeMenu);

// Close menu when clicking on a link
document.querySelectorAll(".nav-links ul li a").forEach((link) => {
  link.addEventListener("click", closeMenu);
});

// Handle scroll behavior
let lastScroll = 0;
const scrollThreshold = 50;

window.addEventListener("scroll", () => {
  const currentScroll = window.pageYOffset;

  if (currentScroll <= 0) {
    navbar.classList.remove("scroll-down");
    return;
  }

  if (currentScroll > lastScroll && currentScroll > scrollThreshold) {
    // Scroll down
    navbar.classList.add("scroll-down");
    navbar.classList.remove("scroll-up");
  } else if (currentScroll < lastScroll) {
    // Scroll up
    navbar.classList.remove("scroll-down");
    navbar.classList.add("scroll-up");
  }

  lastScroll = currentScroll;
});

// Add active class to current page in navigation
const currentLocation = location.href;
const menuItems = document.querySelectorAll(".nav-links ul li a");
menuItems.forEach((item) => {
  if (item.href === currentLocation) {
    item.classList.add("active");
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  });
});

// Mobile Menu Toggle
const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");
const body = document.body;
const navbar = document.querySelector(".navbar");

// Toggle menu when clicking hamburger icon
menuToggle.addEventListener("click", () => {
  navLinks.classList.toggle("active");
  body.classList.toggle("menu-open");
});

// Close menu when clicking on a nav link
document.querySelectorAll(".nav-links a").forEach((link) => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("active");
    body.classList.remove("menu-open");
  });
});

// Close menu when clicking outside of it
document.addEventListener("click", (e) => {
  const isClickInsideNav = navLinks.contains(e.target);
  const isClickInsideToggle = menuToggle.contains(e.target);

  if (
    !isClickInsideNav &&
    !isClickInsideToggle &&
    navLinks.classList.contains("active")
  ) {
    navLinks.classList.remove("active");
    body.classList.remove("menu-open");
  }
});

// Add scroll event listener for navbar
let lastScrollTop = 0;

window.addEventListener("scroll", () => {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  // Add shadow and background opacity based on scroll position
  if (scrollTop > 10) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }

  // Hide/show navbar based on scroll direction
  if (scrollTop > lastScrollTop && scrollTop > 300) {
    // Scrolling down & past threshold
    navbar.classList.add("navbar-hidden");
  } else {
    // Scrolling up
    navbar.classList.remove("navbar-hidden");
  }

  lastScrollTop = scrollTop;
});

// Highlight current page in navigation
const currentPage = window.location.pathname.split("/").pop() || "index.html";
document.querySelectorAll(".nav-links a").forEach((link) => {
  if (link.getAttribute("href") === currentPage) {
    link.classList.add("active");
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    const targetId = this.getAttribute("href");
    if (targetId === "#") return;

    const targetElement = document.querySelector(targetId);
    if (targetElement) {
      const navbarHeight = navbar.offsetHeight;
      const targetPosition =
        targetElement.getBoundingClientRect().top +
        window.pageYOffset -
        navbarHeight;

      window.scrollTo({
        top: targetPosition,
        behavior: "smooth",
      });
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  // DOM Elements
  const navbar = document.querySelector(".navbar");
  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");
  const body = document.body;

  // Mobile Menu Toggle
  if (menuToggle) {
    menuToggle.addEventListener("click", function () {
      navLinks.classList.toggle("active");
      body.classList.toggle("menu-open");
    });
  }

  // Close menu when clicking on links
  if (navLinks) {
    const links = navLinks.querySelectorAll("a");
    links.forEach((link) => {
      link.addEventListener("click", function () {
        navLinks.classList.remove("active");
        body.classList.remove("menu-open");
      });
    });
  }

  // Close menu when clicking outside
  document.addEventListener("click", function (e) {
    if (navLinks && menuToggle) {
      const isClickInsideNav = navLinks.contains(e.target);
      const isClickInsideToggle = menuToggle.contains(e.target);

      if (
        !isClickInsideNav &&
        !isClickInsideToggle &&
        navLinks.classList.contains("active")
      ) {
        navLinks.classList.remove("active");
        body.classList.remove("menu-open");
      }
    }
  });

  // Scroll behavior for navbar
  let lastScrollTop = 0;

  window.addEventListener("scroll", function () {
    if (navbar) {
      const scrollTop =
        window.pageYOffset || document.documentElement.scrollTop;

      // Add shadow and background opacity based on scroll position
      if (scrollTop > 10) {
        navbar.classList.add("scrolled");
      } else {
        navbar.classList.remove("scrolled");
      }

      // Hide/show navbar based on scroll direction
      if (scrollTop > lastScrollTop && scrollTop > 300) {
        // Scrolling down & past threshold
        navbar.classList.add("navbar-hidden");
      } else {
        // Scrolling up
        navbar.classList.remove("navbar-hidden");
      }

      lastScrollTop = scrollTop;
    }
  });

  // Highlight current page in navigation
  if (navLinks) {
    const currentPage =
      window.location.pathname.split("/").pop() || "index.html";
    const links = navLinks.querySelectorAll("a");

    links.forEach((link) => {
      if (link.getAttribute("href") === currentPage) {
        link.classList.add("active");
      }
    });
  }

