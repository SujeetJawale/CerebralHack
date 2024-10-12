// // Handle form submission
// document.getElementById('blogForm').onsubmit = async function (event) {
//     event.preventDefault();

//     const author = document.getElementById('author').value.trim();
//     const content = document.getElementById('content').value.trim();

//     if (author && content) {
//         // Send data to the Flask server
//         const response = await fetch('/submit_blog', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ author, content }),
//         });

//         if (response.ok) {
//             alert('Blog submitted successfully!');
//             loadBlogs();  // Reload blogs
//         } else {
//             alert('Failed to submit the blog.');
//         }
//     } else {
//         alert('Please fill in both the author and content fields.');
//     }
// };

// // Function to load all blogs
// async function loadBlogs() {
//     const response = await fetch('/get_blogs');
//     const blogs = await response.json();

//     const blogsContainer = document.getElementById('blogs');
//     blogsContainer.innerHTML = '';  // Clear previous blogs

//     if (Object.keys(blogs).length === 0) {
//         blogsContainer.innerHTML = '<p>No blogs available yet.</p>';
//     } else {
//         for (const [author, authorBlogs] of Object.entries(blogs)) {
//             authorBlogs.forEach(blog => {
//                 const blogElement = document.createElement('div');
//                 blogElement.classList.add('blog');
//                 blogElement.innerHTML = `<strong>${author}</strong>: ${blog}`;
//                 blogsContainer.appendChild(blogElement);
//             });
//         }
//     }
// }

// // Load blogs on page load
// window.onload = function () {

//     // loadBlogs();
// };

function loading() {
    var t1 = gsap.timeline();

    t1.to("#yellow1", {
        top: "-100%",
        delay: 0.5,
        duration: 0.7,
        ease: "expo.out",
    });

    t1.from(
        "#yellow2",
        {
            top: "100%",
            delay: 0.6,
            duration: 0.7,
            ease: "expo.out",
        },
        "anim"
    );

    t1.to(
        "#loader h1",
        {
            delay: 0.6,
            duration: 0.7,
            color: "black",
        },
        "anim"
    );

    t1.to("#loader", {
        opacity: 0,
    });

    t1.to("#loader", {
        display: "none",
    });
}


function loco() {
    const locoScroll = new LocomotiveScroll({
        el: document.querySelector("#main"),
        smooth: true,
    });

    document.querySelector("#footer h2").addEventListener("click", () => {
        locoScroll.scrollTo(0);
    });
}

loading();
loco();